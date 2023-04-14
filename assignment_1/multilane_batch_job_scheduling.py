from datetime import datetime, timedelta


def preprocess_data(k, data):
    data_dict = {}
    data = data.split('\n')
    for i in range(k):
        line = data[i].strip().split()
        data_dict[i] = line
    return data_dict


def get_current_time(commit_time, run_time):
    dt1 = datetime.strptime(commit_time, '%H%M')
    dt2 = datetime.strptime(run_time, '%H%M')
    delta = timedelta(hours=dt2.hour, minutes=dt2.minute)
    current_time = dt1 + delta
    return current_time


def response_ratio(current_time, cmt_t, r_t):
    delta = timedelta(hours=r_t.hour, minutes=r_t.minute)
    wait_time = current_time - cmt_t
    r = 1 + wait_time / delta
    return r


def find_r_max(r_d):
    r_l = list(r_d.values())
    max_value = max(r_l)
    key_of_max_value = [k for k, v in r_d.items() if v == max_value][0]
    return max_value, key_of_max_value


def MBJS(k, data):
    dd = preprocess_data(k, data)

    dispatch_table = []

    commit_time = dd[0][0]
    run_time = dd[0][1]
    order_num = 1
    job_num = 0
    start_time = commit_time
    dispatch_time = run_time
    dispatch_time_weight = 1
    temp_line = [order_num, job_num, start_time, dispatch_time, dispatch_time_weight]
    dispatch_table.append(temp_line)
    dd.pop(0)
    current_time = get_current_time(commit_time, run_time)

    while len(dd) != 0:
        r_dict = {}
        flag = False
        for i in dd.items():
            commit_time = i[1][0]
            run_time = i[1][1]
            cmt_t = datetime.strptime(commit_time, '%H%M')
            r_t = datetime.strptime(run_time, '%H%M')
            if current_time >= cmt_t:
                flag = True
                r_dict[i[0]] = response_ratio(current_time, cmt_t, r_t)
        if flag:
            max_r, job_num = find_r_max(r_dict)
            order_num += 1
            start_time = current_time
            start_time = start_time.strftime('%H%M')
            commit_time = dd[job_num][0]
            run_time = dd[job_num][1]
            cmt_t = datetime.strptime(commit_time, '%H%M')
            r_t = datetime.strptime(run_time, '%H%M')
            wait_time = current_time - cmt_t
            dispatch_time = wait_time + r_t
            dispatch_time = dispatch_time.strftime('%H%M')
            dispatch_time_weight = max_r
            temp_line = [order_num, job_num, start_time, dispatch_time, round(dispatch_time_weight, 2)]
            dispatch_table.append(temp_line)
            dd.pop(job_num)
            delta = timedelta(hours=r_t.hour, minutes=r_t.minute)
            current_time = current_time + delta
        else:
            commit_time_list = [i[0] for i in dd.values()]
            current_time = min(commit_time_list)
            current_time = datetime.strptime(current_time, '%H%M')
    dispatch_time_list = [datetime.strptime(i[3], '%H%M') for i in dispatch_table]
    dispatch_time_minute_list = [i.hour*60+i.minute for i in dispatch_time_list]
    avg = sum(dispatch_time_minute_list)/k
    w_list = [i[4] for i in dispatch_table]
    avg_w = sum(w_list)/k
    return dispatch_table, round(avg, 2), round(avg_w, 2)

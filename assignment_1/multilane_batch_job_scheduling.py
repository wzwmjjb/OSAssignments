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
    delta = timedelta(minutes=int(run_time))
    current_time = dt1 + delta
    return current_time


def response_ratio(current_time, cmt_t, r_t):
    wait_time = current_time - cmt_t
    r = 1 + wait_time / r_t
    return r


def find_r_max(r_d, dd):
    r_l = list(r_d.values())
    max_value = max(r_l)
    keys_of_max_value = [k for k, v in r_d.items() if v == max_value]
    ddd = {}
    for key in dd:
        if key in keys_of_max_value:
            ddd[key] = dd[key][1]
    min_time = min(ddd.values())
    key_of_max_value = [k for k, v in ddd.items() if v == min_time][0]
    return max_value, key_of_max_value


def MBJS(k, data):
    dd = preprocess_data(k, data)

    dispatch_table = []

    commit_time = dd[0][0]
    run_time = dd[0][1]
    order_num = 1
    job_num = 0
    start_time = commit_time[0:2] + ":" + commit_time[2:4]
    dispatch_time = run_time
    dispatch_time_weight = 1
    temp_line = [order_num, job_num, start_time, str(int(dispatch_time)), dispatch_time_weight]
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
            r_t = timedelta(minutes=int(run_time))
            if current_time >= cmt_t:
                flag = True
                r_dict[i[0]] = response_ratio(current_time, cmt_t, r_t)
        if flag:
            max_r, job_num = find_r_max(r_dict, dd)
            order_num += 1
            start_time = current_time
            start_time = start_time.strftime('%H:%M')
            commit_time = dd[job_num][0]
            run_time = dd[job_num][1]
            cmt_t = datetime.strptime(commit_time, '%H%M')
            r_t = timedelta(minutes=int(run_time))
            wait_time = current_time - cmt_t
            dispatch_time = wait_time + r_t
            dispatch_time = str(int(dispatch_time.seconds / 60))
            dispatch_time_weight = max_r
            temp_line = [order_num, job_num, start_time, dispatch_time, round(dispatch_time_weight, 2)]
            dispatch_table.append(temp_line)
            dd.pop(job_num)
            current_time = current_time + r_t
        else:
            commit_time_list = [i[0] for i in dd.values()]
            current_time = min(commit_time_list)
            current_time = datetime.strptime(current_time, '%H%M')
    dispatch_time_minute_list = [int(i[3]) for i in dispatch_table]
    avg = sum(dispatch_time_minute_list) / k
    w_list = [i[4] for i in dispatch_table]
    avg_w = sum(w_list) / k
    return dispatch_table, round(avg, 2), round(avg_w, 2)


if __name__ == "__main__":
    k = 5
    data = "0830 20\n0900 30\n0900 20\n0910 10\n0920 20"
    MBJS(k, data)
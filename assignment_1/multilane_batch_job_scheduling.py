def preprocess_data(k, data):
    data_dict = {}
    data = data.split('\n')
    for i in range(k):
        line = data[i].strip().split()
        data_dict[i] = line
    return data_dict


def str2time(time):
    hour = str(time)[0:2]
    minute = str(time)[2:4]
    return hour, minute


def time2str(hour, minute):
    time = str(hour) + str(minute)
    return time


def MBJS(k, data):
    dd = preprocess_data(k, data)

    dispatch_table = []

    dispatch_time = dd[0][0]
    cycling_time = dd[0][1]
    temp_line = [1, 0, dispatch_time, cycling_time, 1.0]
    dispatch_table.append(temp_line)
    dd.pop(0)

    while len(dd) != 0:
        break
    return dispatch_table

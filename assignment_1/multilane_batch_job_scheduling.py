def preprocess_data(k, data):
    data_dict = {}
    data = data.split('\n')
    for i in range(k):
        line = data[i].strip().split()
        data_dict[i] = line
    return data_dict


def MBJS(k, data):
    dd = preprocess_data(k, data)
    return dd

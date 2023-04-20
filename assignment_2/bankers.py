import itertools


def get_array(m, arr_str: str):
    arr = arr_str.strip().split('\n')
    if m == 1:
        arr = [[i] for i in arr]
    else:
        arr = [arr_row.split() for arr_row in arr]
    for i in range(len(arr)):
        for j in range(m):
            arr[i][j] = int(arr[i][j])
    return arr


def check_available_sequence(n, m, sequence, allocation_array, max_need_array, ara):
    flag = True
    for i in range(n):
        idx = sequence[i] - 1
        for j in range(m):
            if ara[j] + allocation_array[idx][j] < max_need_array[idx][j]:
                flag = False
                break
        if flag is not True:
            break
        for k in range(m):
            ara[k] += allocation_array[idx][k]
    return flag


def bankers(n_process: int, n_resource: int, allocation_array: str, max_need_array: str, arr_array: str,
            process_num: str, process_request: str):
    allocation_array = get_array(n_resource, allocation_array)
    max_need_array = get_array(n_resource, max_need_array)
    ar_array = get_array(n_resource, arr_array)[0]
    if n_resource == 1:
        for nn in range(n_process):
            ar_array[0] -= allocation_array[nn][0]

    if process_num != "-1":
        pn = int(process_num)
        if n_resource != 1:
            prcs_rqst = process_request.split()
            prcs_rqst = [int(i) for i in prcs_rqst]
        else:
            prcs_rqst = int(process_request)
        for nr in range(n_resource):
            allocation_array[pn-1][nr] += prcs_rqst[nr]
            ar_array[nr] -= prcs_rqst[nr]


    nums = list(range(1, n_process + 1))
    permutations = list(itertools.permutations(nums))
    safe_sequence = []
    for p in permutations:
        ara = [a for a in ar_array]
        if check_available_sequence(n_process, n_resource, p, allocation_array, max_need_array, ara):
            safe_sequence.append(p)
    ss = ""
    for s in safe_sequence:
        for t in s:
            ss += str(t) + " "
        ss += "\n"
    if ss != "":
        return ss
    else:
        ss = "没有安全序列"
        return ss


# if __name__ == "__main__":
#     # n_process = 3
#     # n_resource = 1
#     # allocation_array = "1\n4\n5"
#     # max_need_array = "4\n6\n8"
#     # available_resource_array = "2"
#     n_process = 5
#     n_resource = 4
#     allocation_array = "0 0 1 2\n1 0 0 0\n1 3 5 4\n0 6 3 2\n0 0 1 4"
#     max_need_array = "0 0 1 2\n1 7 5 0\n2 3 5 6\n0 6 5 2 \n0 6 5 6"
#     available_resource_array = "1 5 2 0"
#
#     ss = bankers(n_process, n_resource, allocation_array, max_need_array, available_resource_array, "2", "0 4 2 0")

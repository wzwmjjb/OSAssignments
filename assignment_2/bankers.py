def get_array(arr_str: str):
    arr = arr_str.strip().split('\n')
    arr = [arr_row.split() for arr_row in arr]
    return arr


def bankers(n_process: int, n_resource: int, allocation_array: str, max_need_array: str, available_resource_array: str):
    allocation_array = get_array(allocation_array)
    max_need_array = get_array(max_need_array)
    available_resource_array = get_array(available_resource_array)

    return "123"


if __name__ == "__main__":
    n_process = 5
    n_resource = 4
    allocation_array = "0 0 1 2\n1 0 0 0\n1 3 5 4\n0 6 3 2\n0 0 1 4"
    max_need_array = "0 0 1 2\n1 7 5 0\n2 3 5 6\n0 6 5 2 \n0 6 5 6"
    available_resource_array = "1 5 2 0"

    bankers(n_process, n_resource, allocation_array, max_need_array, available_resource_array)

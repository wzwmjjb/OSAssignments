import random


def random_list(L, k):
    """
    生成一个长度为L，元素值在[1, k]之间的随机列表

    :param L: 列表长度
    :param k: 元素值上限
    :return: 随机列表
    """
    return [random.randint(1, k) for i in range(L)]


def FIFO(page_list, page_num):
    """
    根据页面走向，用FIFO算法计算缺页率和页面置换表

    :param page_list: 页面走向
    :param page_num: 页面数
    :returns: 缺页率, 页面置换表
    """
    page_set = set()
    page_queue = []
    count = 0
    page_table = []
    for page in page_list:
        if page not in page_set:
            page_set.add(page)
            page_queue.append(page)
            if len(page_queue) > page_num:
                page_set.remove(page_queue[0])
                page_queue.pop(0)
            count += 1
            page_table.append(page_queue[:])
        else:
            page_table.append(page_queue[:])
    return count*1.0/len(page_list), page_table


def LRU(page_list, page_num):
    """
    根据页面走向，用LRU算法计算缺页率和页面置换表

    :param page_list: 页面走向
    :param page_num: 页面数
    :returns: 缺页率, 页面置换表
    """
    page_set = set()
    page_queue = []
    count = 0
    page_table = []
    for page in page_list:
        if page not in page_set:
            page_set.add(page)
            page_queue.append(page)
            if len(page_queue) > page_num:
                page_set.remove(page_queue[0])
                page_queue.pop(0)
            count += 1
            page_table.append(page_queue[:])
        else:
            page_queue.remove(page)
            page_queue.append(page)
            page_table.append(page_queue[:])
    return count*1.0/len(page_list), page_table


# def test():
#     page_list = random_list(20, 5)
#     # print(page_list)
#     print(FIFO([7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1], 3))
#     print(LRU([7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1], 3))
#
#
# test()

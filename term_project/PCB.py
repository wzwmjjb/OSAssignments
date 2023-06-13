import random


def random_x():
    """
    随机生成x，其中x的长度是随机生成的，且x中的字符也是1-9之间的随机数字，x以0结尾
    :return:
    """
    length = random.randint(1, 30)
    x = ""
    for i in range(length):
        x += str(random.randint(1, 9))
    x += "0"
    return x


class PCB:
    """
    进程控制块
    """

    def __init__(self, pcb_id: int, status: int, count: int, x: str):
        """
        :param pcb_id:进程标识数
        :param status:进程状态
        :param count:要输出的文件数
        :param x:进程输出时的临时变量
        """
        self.pcb_id = pcb_id
        self.status = status
        self.count = count
        self.x = x
        self.doc = None
        self.doc_len = None

    def __str__(self):
        return "PCB(pcb_id=%d, status=%d, count=%d, x=%s)" % (self.pcb_id, self.status, self.count, self.x)

    def documents(self):
        self.doc = []
        self.doc_len = []
        for i in range(self.count):
            self.doc.append(random_x())
            self.doc_len.append(len(self.doc[i]))
        self.x = self.doc[0]

    def dispatch_user_process(self, remain_buffer, req_block_num, spooling_buffer, first_empty):
        """
        调度用户进程
        :param remain_buffer:输出井剩余容量 c1[i]
        :param req_block_num:空闲输出请求块数 c3
        :param spooling_buffer:输出井 spooling_pool[i]
        :param first_empty:第一个可用空缓冲指针 c2[i][0]
        :return:
        """
        while True:
            if remain_buffer == 0:  # 输出井满
                self.status = 1
                return
            else:
                self.status = 0
                spooling_buffer[first_empty] = self.x
                first_empty = (first_empty + 1) / 100
                remain_buffer -= 1
                self.x = self.x[1:]
                if self.x != "0":
                    break
        if req_block_num == 0:  # 没有空闲输出请求块
            self.status = 3
            return

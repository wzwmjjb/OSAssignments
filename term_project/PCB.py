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

    def __str__(self):
        return "PCB(pcb_id=%d, status=%d, count=%d, x=%s)" % (self.pcb_id, self.status, self.count, self.x)

    def documents(self):
        doc = []
        doc_len = []
        for i in range(self.count):
            doc.append(random_x())
            doc_len.append(len(doc[i]))
        return doc, doc_len

    def dispatch_user_process(self, remain_buffer):
        """
        调度用户进程
        :return:
        """
        if remain_buffer == 0:
            self.status = 1
            return

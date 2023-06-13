import random

from request_block import ReqBlock


def random_x():
    """
    随机生成x，其中x的长度是随机生成的，且x中的字符也是1-9之间的随机数字，x以0结尾
    :return:
    """
    length = random.randint(1, 80)
    x = ""
    for i in range(length):
        x += str(random.randint(1, 9))
    x += "0"
    return x


class PCB:
    """
    进程控制块
    :param pcb_id:进程标识数
    :param status:进程状态
    :param count:要输出的文件数
    :param x:进程输出时的临时变量
    :param doc:要输出的文件集合
    :param doc_len:要输出的文件集合中每个文件的长度
    :param current_doc:当前正在输出的文件指针
    :param doc_first_address:要输出的文件集合中每个文件在输出井中的首地址
    """

    def __init__(self, pcb_id: int, status: int, count: int, x: str):
        self.pcb_id = pcb_id
        self.status = status
        self.count = count
        self.x = x

        self.doc = None
        self.doc_len = None
        self.current_doc = 0
        self.doc_first_address = []

    def __str__(self):
        return "PCB(pcb_id=%d, status=%d, count=%d, x=%s)" % (self.pcb_id, self.status, self.count, self.x)

    def documents(self):
        self.doc = []
        self.doc_len = []
        for i in range(self.count):
            self.doc.append(random_x())
            self.doc_len.append(len(self.doc[i]))
        self.x = self.doc[0]

    def dispatch_user_process(self, remain_buffer: int, req_block_num: int, spooling_buffer: list, first_empty: int,
                              ptr1: int, req_block: ReqBlock):
        """
        调度用户进程，最多完成一个文件的输出，也有可能完成之前没完成的半个文件，或者一个新文件只完成了一半输出井就满了
        :param remain_buffer:输出井剩余容量 c1[i]
        :param req_block_num:空闲输出请求块数 c3
        :param spooling_buffer:输出井 spooling_pool[i]
        :param first_empty:第一个可用空缓冲指针 c2[i][0]
        :param ptr1:空闲请求输出块指针 ptr1
        :param req_block:输出请求块req_blocks[ptr1]
        :return:c1[i], c3, c2[i][0], ptr1
        """
        while True:
            if remain_buffer == 0:  # 输出井满
                self.status = 1
                return remain_buffer, req_block_num, first_empty, ptr1
            else:  # 把文件里的字符输出到输出井
                self.status = 0
                spooling_buffer[first_empty] = self.x[0]
                if len(self.doc_first_address) == self.current_doc:
                    self.doc_first_address.append(first_empty)
                first_empty = (first_empty + 1) % 100
                remain_buffer -= 1
                self.x = self.x[1:]
                if len(self.x) == 0:
                    break

        self.current_doc += 1
        if self.current_doc == self.count:  # 所有文件都输出完毕
            self.status = 4
            return remain_buffer, req_block_num, first_empty, ptr1
        self.x = self.doc[self.current_doc]  # 更新x，读取下一个文件

        if req_block_num == 0:  # 没有空闲输出请求块
            self.status = 3
            return remain_buffer, req_block_num, first_empty, ptr1

        req_block.req_name = self.pcb_id
        # TODO 文件长度大于输出井长度？？？？？先默认不会好了
        req_block.req_length = self.doc_len[self.current_doc - 1]
        req_block.req_address = first_empty
        req_block.req_address = self.doc_first_address[self.current_doc - 1]
        req_block_num -= 1
        ptr1 += 1
        return remain_buffer, req_block_num, first_empty, ptr1


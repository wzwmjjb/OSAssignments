import random


def random_x():
    """
    随机生成x，其中x的长度是随机生成的，且x中的字符也是1-9之间的随机数字，x以0结尾
    :return:
    """
    length = random.randint(1, 50)
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
                              ptr1_: int, req_blocks: list):
        """
        调度用户进程
        :param remain_buffer:输出井剩余容量 c1[i]
        :param req_block_num:空闲输出请求块数 c3
        :param spooling_buffer:输出井 spooling_pool[i]
        :param first_empty:第一个可用空缓冲指针 c2[i][0]
        :param ptr1_:空闲请求输出块指针 ptr1
        :param req_blocks:输出请求块req_blocks
        :return:c1[i], c3, c2[i][0], ptr1_
        """
        while True:
            while True:
                if remain_buffer == 0:  # 输出井满
                    self.status = 1
                    return remain_buffer, req_block_num, first_empty, ptr1_
                else:  # 把文件里的字符输出到输出井
                    spooling_buffer[first_empty] = self.x[0]
                    if len(self.doc_first_address) == self.current_doc:
                        self.doc_first_address.append(first_empty)
                    first_empty = (first_empty + 1) % 100
                    remain_buffer -= 1
                    self.x = self.x[1:]
                    if len(self.x) == 0:
                        break

            self.current_doc += 1

            if req_block_num == 0:  # 没有空闲输出请求块
                self.status = 3
                return remain_buffer, req_block_num, first_empty, ptr1_

            req_blocks[ptr1_].req_name = self.pcb_id
            req_blocks[ptr1_].length = self.doc_len[self.current_doc - 1]
            req_blocks[ptr1_].address = self.doc_first_address[self.current_doc - 1]
            req_block_num -= 1
            ptr1_ = (ptr1_ + 1) % 10
            if self.current_doc == self.count:  # 所有文件都输出完毕
                self.status = 4
                return remain_buffer, req_block_num, first_empty, ptr1_
            else:
                self.x = self.doc[self.current_doc]  # 更新x，读取下一个文件


    def dispatch_spooling_output_process(self, req_blocks: list, ptr0_: int, c1_: list, c2_: list, user_states: list,
                                         c3_: int, spooling_buffer_: list):
        """
        输出井进程
        :param req_blocks:输出请求块req_blocks
        :param ptr0_:要输出的第一个请求输出块指针
        :param c1_:输出井剩余容量 [c1[0], c1[1]]
        :param c2_:输出井使用情况 [第一个可用空缓冲指针, 第一个满缓冲指针]
        :param user_states:[用户进程0状态, 用户进程1状态]
        :param c3_:输出请求块数
        :param spooling_buffer_:输出井[spoolling_pool0, spoolling_pool1]
        :return:ptr0_, c3_, output_info, user_states
        """
        output_info = []
        while True:
            if c3_ == 10:
                if user_states[0] == 4 and user_states[1] == 4:
                    self.status = 4
                else:
                    self.status = 2
                return ptr0_, c3_, output_info, user_states

            user_process_id = req_blocks[ptr0_].req_name
            text_length = req_blocks[ptr0_].length
            text_address = req_blocks[ptr0_].address
            text_end = (text_address + text_length) % 100
            if text_address < text_end:
                text = spooling_buffer_[user_process_id][text_address:text_end]
            else:
                text = spooling_buffer_[user_process_id][text_address:] + spooling_buffer_[user_process_id][:text_end]
            texts = ""
            for i in range(len(text)):
                texts += text[i]
            output_info.append("用户进程%d输出文件：%s" % (user_process_id, texts))
            ptr0_ = (ptr0_ + 1) % 10
            c3_ += 1
            c1_[user_process_id] += text_length
            c2_[user_process_id][1] = (c2_[user_process_id][1] + text_length) % 100
            if user_states[user_process_id] == 1:
                user_states[user_process_id] = 0
                return ptr0_, c3_, output_info, user_states
            if user_states[user_process_id] == 3:
                user_states[user_process_id] = 0
                return ptr0_, c3_, output_info, user_states

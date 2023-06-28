import random

from request_block import ReqBlock
from term_project.PCB import PCB


class SpoolingServer:
    """
    SPOOLing输出服务程序
    :param user0:用户进程0
    :param user1:用户进程1
    :param spooling_pool:输出井
    :param c1:输出井可用容量
    :param c2:输出井使用情况 [第一个可用空缓冲指针, 第一个满缓冲指针]
    :param c3:输出请求块数
    :param ptr0:要输出的第一个请求输出块指针
    :param ptr1:空闲请求输出块指针
    :param spooling_process:SPOOLing执行进程
    :param dispatch_info:调度信息
    :param output_info:输出信息
    """

    def __init__(self, file_num0: int, file_num1: int):
        # 初始化两个用户的PCB
        self.user0 = PCB(0, 0, file_num0, "")
        self.user1 = PCB(1, 0, file_num1, "")
        self.user0.documents()
        self.user1.documents()
        # 初始化两个用户的输出井
        self.spooling_pool = [[" " for i in range(100)], [" " for i in range(100)]]
        self.c1 = [100, 100]
        self.c2 = [[0, 0], [0, 0]]
        # 初始化输出请求块
        self.c3 = 10
        self.req_blocks = [ReqBlock(0, 0, 0) for i in range(self.c3)]
        self.ptr0 = 0
        self.ptr1 = 0
        # 初始化SPOOLing执行进程
        self.spooling_process = PCB(2, 2, 0, "")

        # 调度信息
        self.dispatch_info = []
        # 输出信息
        self.output_info = []

    def random_dispatch(self, first_time_append: list):
        """
        随机调度
        :param first_time_append:[用户进程0结束, 用户进程1结束]
        :return:
        """
        if self.user0.status == 0 and self.user1.status == 0 and self.spooling_process.status == 0:
            x = random.randint(1, 100)
        elif self.user0.status != 0 and self.user1.status == 0 and self.spooling_process.status == 0:
            x = random.randint(46, 100)
        elif self.user0.status == 0 and self.user1.status != 0 and self.spooling_process.status == 0:
            x = random.randint(46, 100)
            if 46 <= x <= 90:
                x -= 45
        elif self.user0.status == 0 and self.user1.status == 0 and self.spooling_process.status != 0:
            x = random.randint(1, 90)
        elif self.user0.status == 0 and self.user1.status != 0 and self.spooling_process.status != 0:
            x = 1
        elif self.user0.status != 0 and self.user1.status == 0 and self.spooling_process.status != 0:
            x = 46
        elif self.user0.status != 0 and self.user1.status != 0 and self.spooling_process.status == 0:
            x = 91
        else:
            x = random.randint(1, 100)

        if x <= 45:
            if self.user0.status == 0:  # 执行用户进程0
                self.c1[0], self.c3, self.c2[0][0], self.ptr1 = self.user0.dispatch_user_process(self.c1[0], self.c3,
                                                                                                 self.spooling_pool[0],
                                                                                                 self.c2[0][0],
                                                                                                 self.ptr1,
                                                                                                 self.req_blocks)
                if self.spooling_process.status != 0:
                    self.spooling_process.status = 0
                self.dispatch_info.append("执行用户进程0，输出字符到输出井，处于执行状态0\n")
            if self.user0.status == 1:  # 输出井0满
                self.dispatch_info.append("用户进程0输出井0满，处于等待状态1\n")
            if self.user0.status == 3:  # 没有空闲输出请求块
                self.dispatch_info.append("用户进程0没有空闲输出请求块，处于等待状态3\n")
            if self.user0.status == 4:  # 执行结束
                if first_time_append[0]:
                    self.dispatch_info.append("用户进程0执行结束，处于终止状态4\n")
                    first_time_append[0] = False
        elif x <= 90:
            if self.user1.status == 0:
                self.c1[1], self.c3, self.c2[1][0], self.ptr1 = self.user1.dispatch_user_process(self.c1[1], self.c3,
                                                                                                 self.spooling_pool[1],
                                                                                                 self.c2[1][0],
                                                                                                 self.ptr1,
                                                                                                 self.req_blocks)
                if self.spooling_process.status != 0:
                    self.spooling_process.status = 0
                self.dispatch_info.append("执行用户进程1，输出字符到输出井，处于执行状态0\n")
            if self.user1.status == 1:
                self.dispatch_info.append("用户进程1输出井1满，处于等待状态1\n")
            if self.user1.status == 3:
                self.dispatch_info.append("用户进程1没有空闲输出请求块，处于等待状态3\n")
            if self.user1.status == 4:
                if first_time_append[1]:
                    self.dispatch_info.append("用户进程1执行结束，处于终止状态4\n")
                    first_time_append[1] = False
        elif x <= 100:
            if self.spooling_process.status == 0:
                self.ptr0, self.c3, opif, us, self.ptr1 = self.spooling_process.dispatch_spooling_output_process(
                    self.req_blocks,
                    self.ptr0,
                    self.c1,
                    self.c2,
                    [self.user0.status, self.user1.status],
                    self.c3,
                    self.spooling_pool,
                    [self.user0.spare_req_block, self.user1.spare_req_block],
                    self.ptr1)
                self.user0.status = us[0]
                self.user1.status = us[1]
                for i in range(len(opif)):
                    self.output_info.append(opif[i])
                self.dispatch_info.append("SPOOLing执行进程处于执行状态0\n")
            if self.spooling_process.status == 2:
                self.dispatch_info.append("请求输出块为空，SPOOLing执行进程处于等待状态2\n")
            if self.spooling_process.status == 4:
                self.dispatch_info.append("SPOOLing执行进程已经完成，处于终止状态4\n")
            else:
                pass


if __name__ == '__main__':
    spooling = SpoolingServer(10, 10)
    first_time = [True, True]
    while spooling.spooling_process.status != 4:
        spooling.random_dispatch(first_time)

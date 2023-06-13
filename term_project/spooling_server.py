import random

from term_project.PCB import PCB


class SpoolingServer:
    """
    SPOOLing输出服务程序
    : param user0:用户进程0
    : param user1:用户进程1
    : param spooling_pool:输出井
    : param c1:输出井可用容量
    : param c2:输出井使用情况 [第一个可用空缓冲指针, 第一个满缓冲指针]
    : param c3:输出请求块数
    : param ptr0:要输出的第一个请求输出块指针
    : param ptr1:空闲请求输出块指针
    : param spooling_process:SPOOLing执行进程
    """

    def __init__(self, file_num0: int, file_num1: int):
        # 初始化两个用户的PCB
        self.user0 = PCB(0, 0, file_num0, "")
        self.user1 = PCB(1, 0, file_num1, "")
        self.user0.documents()
        self.user1.documents()
        # 初始化两个用户的输出井
        self.spooling_pool = [[], []]
        self.c1 = [100, 100]
        self.c2 = [[0, 0], [0, 0]]
        # 初始化输出请求块
        self.c3 = 10
        self.ptr0 = 0
        self.ptr1 = 0
        # 初始化SPOOLing执行进程
        self.spooling_process = PCB(2, 0, 0, "")

    def random_dispatch(self):
        """
        :return:
        """
        x = random.randint(1, 100)
        if x <= 45:
            if self.user0.status == 0:  # 执行用户进程0
                pass
            elif self.user0.status == 1:  # 输出井0满
                pass
            elif self.user0.status == 3:  # 没有空闲输出请求块
                pass
            else:
                pass
        elif x <= 90:
            pass
        elif self.spooling_process.status == 0:
            pass  # 执行SPOOLing进程
        else:
            pass


if __name__ == '__main__':
    spooling = SpoolingServer(3, 5)
    while (spooling.user0.status != 4 or spooling.user1.status != 4):
        spooling.random_dispatch()
    print("hh")

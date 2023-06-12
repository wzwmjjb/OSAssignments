from term_project.PCB import PCB


class SpoolingServer:
    """
    SPOOLing输出服务程序
    """

    def __init__(self, file_num0: int, file_num1: int):
        # 初始化两个用户的PCB
        self.user0 = PCB(0, 0, file_num0, "")
        self.user1 = PCB(1, 0, file_num1, "")
        # 初始化两个用户的输出井
        self.spooling_pool = [[], []]
        self.c1 = [100, 100]
        self.c2 = [[0, 0], [0, 0]]
        # 初始化输出请求块
        self.c3 = 10
        self.ptr0 = 0
        self.ptr1 = 0

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
        return "PCB(pcb_id=%d, status=%d, count=%d, x=%d)" % (self.pcb_id, self.status, self.count, self.x)

class ReqBlock:
    """
    请求输出块
    """

    def __init__(self, req_name: int, length: int, address: int):
        """
        :param req_name:请求进程名
        :param length:本次输出信息长度
        :param address:信息在输出井的首地址
        """
        self.req_name = req_name
        self.length = length
        self.address = address

    def __str__(self):
        return "ReqBlock(req_name=%s, length=%d, address=%d)" % (self.req_name, self.length, self.address)

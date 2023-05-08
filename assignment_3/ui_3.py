"""
用PYQT5实现一个简单的GUI程序，要求如下：
1. 输入页面走向长度L，内存块数目page_num，页表长度k
2. 用随机数生成页面走向
3. 分别用FIFO和LRU算法计算缺页率和页面置换表
4. 将缺页率用标签显示在窗口上，页面置换表用表格显示在窗口上
"""
import sys

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QHBoxLayout, QVBoxLayout, \
    QApplication, QTableWidgetItem

from assignment_3.page_displacement import FIFO, random_list, LRU


class UI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lbl_L = QLabel("请输入页面走向长度：")
        self.edit_L = QLineEdit()

        self.lbl_page_num = QLabel("请输入内存块数目：  ")
        self.edit_page_num = QLineEdit()

        self.lbl_k = QLabel("请输入页表长度：    ")
        self.edit_k = QLineEdit()

        self.btn_ok = QPushButton("确定")
        self.btn_ok.clicked.connect(self.on_click)

        self.lbl_FIFO_result = QLabel("FIFO缺页率：0")
        self.lbl_LRU_result = QLabel("LRU缺页率：0")

        self.FIFO_table = QTableWidget()
        self.LRO_table = QTableWidget()

        hbox = QHBoxLayout()
        hbox.addWidget(self.lbl_L)
        hbox.addWidget(self.edit_L)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.lbl_page_num)
        hbox2.addWidget(self.edit_page_num)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.lbl_k)
        hbox3.addWidget(self.edit_k)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addWidget(self.btn_ok)
        vbox.addWidget(self.lbl_FIFO_result)
        vbox.addWidget(self.FIFO_table)
        vbox.addWidget(self.lbl_LRU_result)
        vbox.addWidget(self.LRO_table)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 850, 1000)
        self.setWindowTitle('页面置换算法')

        self.show()

    def on_click(self):
        try:
            L = int(self.edit_L.text())
            page_num = int(self.edit_page_num.text())
            k = int(self.edit_k.text())
            page_list = random_list(L, k)
            FIFO_result, FIFO_table = FIFO(page_list, page_num)
            LRU_result, LRU_table = LRU(page_list, page_num)
            self.lbl_FIFO_result.setText("FIFO缺页率：" + str(FIFO_result))
            self.lbl_LRU_result.setText("LRU缺页率：" + str(LRU_result))
            self.FIFO_table.setColumnCount(L)
            self.FIFO_table.setRowCount(page_num)
            self.LRO_table.setColumnCount(L)
            self.LRO_table.setRowCount(page_num)

            for i in range(L):
                if len(FIFO_table[i]) == page_num:
                    for j in range(page_num):
                        self.FIFO_table.setItem(j, i, QTableWidgetItem(str(FIFO_table[i][j])))
                else:
                    for j in range(len(FIFO_table[i])):
                        self.FIFO_table.setItem(j, i, QTableWidgetItem(str(FIFO_table[i][j])))
                    for j in range(len(FIFO_table[i]), page_num):
                        self.FIFO_table.setItem(j, i, QTableWidgetItem(" "))

            for i in range(L):
                if len(LRU_table[i]) == page_num:
                    for j in range(page_num):
                        self.LRO_table.setItem(j, i, QTableWidgetItem(str(LRU_table[i][j])))
                else:
                    for j in range(len(LRU_table[i])):
                        self.LRO_table.setItem(j, i, QTableWidgetItem(str(LRU_table[i][j])))
                    for j in range(len(LRU_table[i]), page_num):
                        self.LRO_table.setItem(j, i, QTableWidgetItem(" "))
        except:
            self.lbl_FIFO_result.setText("输入有误！")
            self.lbl_LRU_result.setText("输入有误！")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())

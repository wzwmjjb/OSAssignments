import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QTextEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QMessageBox, QTableWidget, QTableWidgetItem

from assignment_1.multilane_batch_job_scheduling import MBJS


class UI(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # 创建标签和文本框
        self.lbl_k = QLabel("请输入k的值：")
        self.edit_k = QLineEdit()

        self.lbl_data = QLabel("请输入数据：")
        self.edit_data = QTextEdit()

        # 创建按钮
        self.btn_ok = QPushButton("确定")
        self.btn_ok.clicked.connect(self.on_click)

        # 创建表格
        self.table = QTableWidget()
        self.table.setColumnCount(5)  # 设置表格列数
        self.table.setHorizontalHeaderLabels(['调度次序', '作业号', '调度时间', '周转时间', '带权周转时间'])  # 设置表头
        self.table.verticalHeader().hide()

        # 创建标签
        self.lbl_avg = QLabel("平均周转时间：0")
        self.lbl_avg_w = QLabel("平均带权周转时间：0")

        # 创建水平布局
        hbox = QHBoxLayout()
        hbox.addWidget(self.lbl_k)
        hbox.addWidget(self.edit_k)

        # 创建垂直布局
        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.lbl_data)
        vbox.addWidget(self.edit_data)
        vbox.addWidget(self.btn_ok)
        vbox.addWidget(self.table)
        vbox.addWidget(self.lbl_avg)
        vbox.addWidget(self.lbl_avg_w)

        # 设置窗口布局
        self.setLayout(vbox)

        # 设置窗口大小和位置
        self.setGeometry(300, 300, 850, 1000)
        self.setWindowTitle('多道批处理作业调度')

        self.show()

    def on_click(self):
        try:
            k = int(self.edit_k.text())
            data = self.edit_data.toPlainText()
            dispatch_table = MBJS(k, data)
            print(dispatch_table)

            # 清空表格
            self.table.clearContents()
            self.table.setRowCount(k)

            # 添加数据
            for i in range(k):  # todo 更改表格内数据
                item1 = QTableWidgetItem(str(i + 1))
                item2 = QTableWidgetItem("job_" + str(i))
                item3 = QTableWidgetItem(str(i * 10))
                item4 = QTableWidgetItem(str(i * 20))
                item5 = QTableWidgetItem(str(i * 30))
                self.table.setItem(i, 0, item1)
                self.table.setItem(i, 1, item2)
                self.table.setItem(i, 2, item3)
                self.table.setItem(i, 3, item4)
                self.table.setItem(i, 4, item5)

            # 添加平均时间
            avg = 1
            avg_w = 2  # todo 更改两个时间
            self.lbl_avg.setText("平均周转时间：" + str(avg))
            self.lbl_avg_w.setText("平均加权周转时间：" + str(avg_w))
        except:
            QMessageBox.about(self, "提示", "输入格式错误，请检查输入的格式")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())

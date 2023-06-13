import sys
import time

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QHBoxLayout, \
    QVBoxLayout, QHeaderView, QTextEdit, QMessageBox

from term_project.spooling_server import SpoolingServer


class UI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        vbox_left = QVBoxLayout()
        self.file_num0 = QLabel("用户0文件数:")
        self.edit_file_num0 = QLineEdit()
        hbox_file_num0 = QHBoxLayout()
        hbox_file_num0.addWidget(self.file_num0)
        hbox_file_num0.addWidget(self.edit_file_num0)
        vbox_left.addLayout(hbox_file_num0)

        self.file_num1 = QLabel("用户1文件数:")
        self.edit_file_num1 = QLineEdit()
        hbox_file_num1 = QHBoxLayout()
        hbox_file_num1.addWidget(self.file_num1)
        hbox_file_num1.addWidget(self.edit_file_num1)
        vbox_left.addLayout(hbox_file_num1)

        self.btn_ok = QPushButton("确定")
        self.btn_ok.clicked.connect(self.on_click)
        vbox_left.addWidget(self.btn_ok)

        self.spooling_pool0 = QLabel("输出井0：")
        self.spooling_pool0_input = QTableWidget()
        self.spooling_pool0_input.setRowCount(10)
        self.spooling_pool0_input.setColumnCount(10)
        self.spooling_pool0_input.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.spooling_pool0_input.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.spooling_pool0_input.verticalHeader().setVisible(False)
        self.spooling_pool0_input.horizontalHeader().setVisible(False)
        vbox_spooling_pool0 = QVBoxLayout()
        vbox_spooling_pool0.addWidget(self.spooling_pool0)
        vbox_spooling_pool0.addWidget(self.spooling_pool0_input)
        vbox_left.addLayout(vbox_spooling_pool0)

        self.spooling_pool1 = QLabel("输出井1：")
        self.spooling_pool1_input = QTableWidget()
        self.spooling_pool1_input.setRowCount(10)
        self.spooling_pool1_input.setColumnCount(10)
        self.spooling_pool1_input.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.spooling_pool1_input.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.spooling_pool1_input.verticalHeader().setVisible(False)
        self.spooling_pool1_input.horizontalHeader().setVisible(False)
        vbox_spooling_pool1 = QVBoxLayout()
        vbox_spooling_pool1.addWidget(self.spooling_pool1)
        vbox_spooling_pool1.addWidget(self.spooling_pool1_input)
        vbox_left.addLayout(vbox_spooling_pool1)

        self.c1_label = QLabel("输出井剩余空间：")
        self.c1 = QTableWidget()
        self.c1.setRowCount(1)
        self.c1.setColumnCount(2)
        self.c1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.c1.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.c1.setHorizontalHeaderLabels(["输出井0", "输出井1"])
        self.c1.setVerticalHeaderLabels(["输出井剩余空间"])
        self.c1.resizeColumnsToContents()
        self.c1.resizeRowsToContents()

        self.c2_label = QLabel("输出井使用情况：")
        self.c2 = QTableWidget()
        self.c2.setRowCount(2)
        self.c2.setColumnCount(2)
        self.c2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.c2.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.c2.setHorizontalHeaderLabels(["可用空缓冲指针", "满缓冲指针"])
        self.c2.setVerticalHeaderLabels(["输出井0", "输出井1"])
        self.c2.resizeColumnsToContents()
        self.c2.resizeRowsToContents()

        vbox_c1_c2 = QVBoxLayout()
        vbox_c1_c2.addWidget(self.c1_label)
        vbox_c1_c2.addWidget(self.c1)
        vbox_c1_c2.addWidget(self.c2_label)
        vbox_c1_c2.addWidget(self.c2)
        vbox_left.addLayout(vbox_c1_c2)

        self.c3_label = QLabel("输出请求块剩余数：")
        self.c3_value = QLabel("10")
        hbox_c3 = QHBoxLayout()
        hbox_c3.addWidget(self.c3_label)
        hbox_c3.addWidget(self.c3_value)
        vbox_left.addLayout(hbox_c3)

        self.ptr0_label = QLabel("ptr0：")
        self.ptr0_value = QLabel("0")
        hbox_ptr0 = QHBoxLayout()
        hbox_ptr0.addWidget(self.ptr0_label)
        hbox_ptr0.addWidget(self.ptr0_value)
        vbox_left.addLayout(hbox_ptr0)

        self.ptr1_label = QLabel("ptr1：")
        self.ptr1_value = QLabel("0")
        hbox_ptr1 = QHBoxLayout()
        hbox_ptr1.addWidget(self.ptr1_label)
        hbox_ptr1.addWidget(self.ptr1_value)
        vbox_left.addLayout(hbox_ptr1)

        vbox_middle = QVBoxLayout()

        self.user0_label = QLabel("用户进程0文件：")
        self.user0_value = QTableWidget()
        self.user0_value.setColumnCount(3)
        self.user0_value.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.user0_value.setHorizontalHeaderLabels(["文件序号", "文件长度", "文件内容"])
        self.user0_value.resizeColumnsToContents()
        vbox_middle.addWidget(self.user0_label)
        vbox_middle.addWidget(self.user0_value)

        self.user1_label = QLabel("用户进程1文件：")
        self.user1_value = QTableWidget()
        self.user1_value.setColumnCount(3)
        self.user1_value.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.user1_value.setHorizontalHeaderLabels(["文件序号", "文件长度", "文件内容"])
        self.user1_value.resizeColumnsToContents()
        vbox_middle.addWidget(self.user1_label)
        vbox_middle.addWidget(self.user1_value)

        vbox_right = QVBoxLayout()
        self.output_lable = QLabel("输出文件：")
        self.output_value = QTextEdit()
        vbox_right.addWidget(self.output_lable)
        vbox_right.addWidget(self.output_value)

        self.dispatch_label = QLabel("调度信息：")
        self.dispatch_value = QTextEdit()
        vbox_right.addWidget(self.dispatch_label)
        vbox_right.addWidget(self.dispatch_value)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox_left, 1)
        hbox.addLayout(vbox_middle, 2)
        hbox.addLayout(vbox_right, 2)
        self.setLayout(hbox)

        self.showMaximized()
        self.setWindowTitle('SPOOLing')
        self.show()

    def on_click(self):
        """
        获取用户进程输入的文件数量
        :return:
        """
        try:
            file_num0 = int(self.edit_file_num0.text())
            file_num1 = int(self.edit_file_num1.text())
        except:
            QMessageBox.warning(self, "警告", "请输入正确的文件数量")
            return
        SpoolingServer(file_num0, file_num1)
        # 按秒刷新界面
        # for i in range(1, 11):
        #     self.spooling_pool0_input.setText(str(i))
        #     app.processEvents()
        #     time.sleep(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())

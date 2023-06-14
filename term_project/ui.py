import sys
import time

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTableWidget, QHBoxLayout, \
    QVBoxLayout, QHeaderView, QTextEdit, QMessageBox, QTableWidgetItem

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
        vbox_left.addLayout(vbox_spooling_pool0, 1)

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
        vbox_left.addLayout(vbox_spooling_pool1, 1)

        self.c1c2_label = QLabel("输出井剩余空间和使用情况：")
        self.c1c2 = QTableWidget()
        self.c1c2.setRowCount(3)
        self.c1c2.setColumnCount(2)
        self.c1c2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.c1c2.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.c1c2.setHorizontalHeaderLabels(["输出井0", "输出井1"])
        self.c1c2.setVerticalHeaderLabels(["输出井剩余空间", "可用空缓冲指针", "满缓冲指针"])
        self.c1c2.resizeColumnsToContents()
        self.c1c2.resizeRowsToContents()
        self.c1c2.setItem(0, 0, QTableWidgetItem("100"))
        self.c1c2.setItem(0, 1, QTableWidgetItem("100"))
        self.c1c2.setItem(1, 0, QTableWidgetItem("0"))
        self.c1c2.setItem(1, 1, QTableWidgetItem("0"))
        self.c1c2.setItem(2, 0, QTableWidgetItem("0"))
        self.c1c2.setItem(2, 1, QTableWidgetItem("0"))

        vbox_c1_c2 = QVBoxLayout()
        vbox_c1_c2.addWidget(self.c1c2_label)
        vbox_c1_c2.addWidget(self.c1c2)
        vbox_left.addLayout(vbox_c1_c2)

        self.c3_label = QLabel("输出请求块剩余数：")
        self.c3_value = QLabel("10")
        hbox_c3 = QHBoxLayout()
        hbox_c3.addWidget(self.c3_label)
        hbox_c3.addWidget(self.c3_value)
        vbox_left.addLayout(hbox_c3)

        self.ptr0_label = QLabel("输出请求输出块指针：")
        self.ptr0_value = QLabel("0")
        hbox_ptr0 = QHBoxLayout()
        hbox_ptr0.addWidget(self.ptr0_label)
        hbox_ptr0.addWidget(self.ptr0_value)
        vbox_left.addLayout(hbox_ptr0)

        self.ptr1_label = QLabel("空闲请求输出块指针：")
        self.ptr1_value = QLabel("0")
        hbox_ptr1 = QHBoxLayout()
        hbox_ptr1.addWidget(self.ptr1_label)
        hbox_ptr1.addWidget(self.ptr1_value)
        vbox_left.addLayout(hbox_ptr1)

        self.process_states = QLabel("进程状态：")
        self.user0_state_label = QLabel("      用户进程0")
        self.user1_state_label = QLabel("      用户进程1")
        self.spooling_state_label = QLabel("      SPOOLing输出进程")
        self.user0_state_label.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.user1_state_label.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.spooling_state_label.setStyleSheet("background-color: rgb(255, 165, 0);")

        self.vbox_process_states = QVBoxLayout()
        self.vbox_process_states.addWidget(self.process_states)
        self.vbox_process_states.addWidget(self.user0_state_label)
        self.vbox_process_states.addWidget(self.user1_state_label)
        self.vbox_process_states.addWidget(self.spooling_state_label)
        vbox_left.addLayout(self.vbox_process_states)

        vbox_middle = QVBoxLayout()

        self.user0_label = QLabel("用户进程0文件：")
        self.user0_value = QTableWidget()
        self.user0_value.setColumnCount(3)
        self.user0_value.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.user0_value.setHorizontalHeaderLabels(["文件序号", "文件长度", "文件内容"])
        self.user0_value.resizeColumnsToContents()
        self.user0_value.verticalHeader().setVisible(False)
        vbox_middle.addWidget(self.user0_label)
        vbox_middle.addWidget(self.user0_value)

        self.user1_label = QLabel("用户进程1文件：")
        self.user1_value = QTableWidget()
        self.user1_value.setColumnCount(3)
        self.user1_value.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.user1_value.setHorizontalHeaderLabels(["文件序号", "文件长度", "文件内容"])
        self.user1_value.resizeColumnsToContents()
        self.user1_value.verticalHeader().setVisible(False)
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

    def set_process_state_color(self, process_state_label: QLabel, status: int):
        if status == 0:
            process_state_label.setStyleSheet("background-color: rgb(0, 255, 0);")
        elif status == 1:
            process_state_label.setStyleSheet("background-color: rgb(255, 0, 0);")
        elif status == 2:
            process_state_label.setStyleSheet("background-color: rgb(255, 165, 0);")
        elif status == 3:
            process_state_label.setStyleSheet("background-color: rgb(255, 255, 0);")
        elif status == 4:
            process_state_label.setStyleSheet("background-color: rgb(0, 255, 255);")

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

        spooling_ = SpoolingServer(file_num0, file_num1)
        self.user0_state_label.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.user1_state_label.setStyleSheet("background-color: rgb(0, 255, 0);")
        self.spooling_state_label.setStyleSheet("background-color: rgb(255, 165, 0);")

        self.user0_value.setRowCount(len(spooling_.user0.doc_len))
        for i in range(len(spooling_.user0.doc)):
            self.user0_value.setItem(i, 0, QTableWidgetItem(str(i)))
            self.user0_value.setItem(i, 1, QTableWidgetItem(str(spooling_.user0.doc_len[i])))
            self.user0_value.setItem(i, 2, QTableWidgetItem(spooling_.user0.doc[i]))
        self.user1_value.setRowCount(len(spooling_.user1.doc_len))
        for i in range(len(spooling_.user1.doc)):
            self.user1_value.setItem(i, 0, QTableWidgetItem(str(i)))
            self.user1_value.setItem(i, 1, QTableWidgetItem(str(spooling_.user1.doc_len[i])))
            self.user1_value.setItem(i, 2, QTableWidgetItem(spooling_.user1.doc[i]))

        first_time = [True, True]
        while spooling_.spooling_process.status != 4:
            spooling_.random_dispatch(first_time)

            for i in range(10):
                for j in range(10):
                    self.spooling_pool0_input.setItem(i, j, QTableWidgetItem(spooling_.spooling_pool[0][i * 10 + j]))
                    self.spooling_pool1_input.setItem(i, j, QTableWidgetItem(spooling_.spooling_pool[1][i * 10 + j]))

            for i in range(10):
                for j in range(10):
                    if spooling_.c2[0][1] > spooling_.c2[0][0]:
                        if (0 <= i * 10 + j < spooling_.c2[0][0]) or (
                                spooling_.c2[0][1] <= i * 10 + j <= 99):
                            self.spooling_pool0_input.item(i, j).setBackground(QColor(0, 255, 255))
                        else:
                            self.spooling_pool0_input.item(i, j).setBackground(QColor(255, 255, 255))
                    elif spooling_.c2[0][1] < spooling_.c2[0][0]:
                        if spooling_.c2[0][1] <= i * 10 + j < spooling_.c2[0][0]:
                            self.spooling_pool0_input.item(i, j).setBackground(QColor(0, 255, 255))
                        else:
                            self.spooling_pool0_input.item(i, j).setBackground(QColor(255, 255, 255))
                    elif spooling_.c1[0] == 0:
                        self.spooling_pool0_input.item(i, j).setBackground(QColor(0, 255, 255))
            for i in range(10):
                for j in range(10):
                    if spooling_.c2[1][1] > spooling_.c2[1][0]:
                        if (0 <= i * 10 + j < spooling_.c2[1][0]) or (
                                spooling_.c2[1][1] <= i * 10 + j <= 99):
                            self.spooling_pool1_input.item(i, j).setBackground(QColor(0, 255, 255))
                        else:
                            self.spooling_pool1_input.item(i, j).setBackground(QColor(255, 255, 255))
                    elif spooling_.c2[1][1] < spooling_.c2[1][0]:
                        if spooling_.c2[1][1] <= i * 10 + j < spooling_.c2[1][0]:
                            self.spooling_pool1_input.item(i, j).setBackground(QColor(0, 255, 255))
                        else:
                            self.spooling_pool1_input.item(i, j).setBackground(QColor(255, 255, 255))
                    elif spooling_.c1[1] == 0:
                        self.spooling_pool1_input.item(i, j).setBackground(QColor(0, 255, 255))
            temp_before = []
            for i in range(3):
                tb = []
                for j in range(2):
                    tb.append(self.c1c2.item(i, j).text())
                temp_before.append(tb)
            self.c1c2.setItem(0, 0, QTableWidgetItem(str(spooling_.c1[0])))
            self.c1c2.setItem(0, 1, QTableWidgetItem(str(spooling_.c1[1])))
            self.c1c2.setItem(1, 0, QTableWidgetItem(str(spooling_.c2[0][0])))
            self.c1c2.setItem(1, 1, QTableWidgetItem(str(spooling_.c2[0][1])))
            self.c1c2.setItem(2, 0, QTableWidgetItem(str(spooling_.c2[1][0])))
            self.c1c2.setItem(2, 1, QTableWidgetItem(str(spooling_.c2[1][1])))
            for i in range(3):
                for j in range(2):
                    if temp_before[i][j] != self.c1c2.item(i, j).text():
                        self.c1c2.item(i, j).setForeground(QColor(255, 0, 0))

            temp_before = self.c3_value.text()
            self.c3_value.setText(str(spooling_.c3))
            if temp_before != self.c3_value.text():
                self.c3_value.setStyleSheet("color: rgb(255, 0, 0);")

            temp_before = self.ptr0_value.text()
            self.ptr0_value.setText(str(spooling_.ptr0))
            if temp_before != self.ptr0_value.text():
                self.ptr0_value.setStyleSheet("color: rgb(255, 0, 0);")

            temp_before = self.ptr1_value.text()
            self.ptr1_value.setText(str(spooling_.ptr1))
            if temp_before != self.ptr1_value.text():
                self.ptr1_value.setStyleSheet("color: rgb(255, 0, 0);")

            di = ""
            for info in spooling_.dispatch_info:
                di += info
            oi = ""
            for info in spooling_.output_info:
                oi += info + "\n"
            self.dispatch_value.setText(di)
            self.output_value.setText(oi)

            self.set_process_state_color(self.user0_state_label, spooling_.user0.status)
            self.set_process_state_color(self.user1_state_label, spooling_.user1.status)
            self.set_process_state_color(self.spooling_state_label, spooling_.spooling_process.status)

            app.processEvents()
            time.sleep(2)
        QMessageBox.information(self, "提示", "作业已完成")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())

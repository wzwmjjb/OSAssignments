import sys

from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QTextEdit, QHBoxLayout, QVBoxLayout, QPushButton, QApplication

from assignment_2.bankers import bankers


class UI(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        self.lbl_process = QLabel("请输入进程数：")
        self.edit_process = QLineEdit()

        self.lbl_resource = QLabel("请输入资源数：")
        self.edit_resource = QLineEdit()

        self.lbl_allocation = QLabel("请输入分配矩阵：")
        self.edit_allocation = QTextEdit()

        self.lbl_max_need = QLabel("请输入最大需求矩阵：")
        self.edit_max_need = QTextEdit()

        self.lbl_available = QLabel("请输入可用资源矩阵：")
        self.edit_available = QTextEdit()

        self.btn_ok = QPushButton("确定")
        self.btn_ok.clicked.connect(self.on_click)

        self.lbl_safe_sequences = QLabel("所有安全序列：")
        self.edit_safe_sequences = QTextEdit()

        hbox1 = QHBoxLayout()
        hbox1.addWidget(self.lbl_process)
        hbox1.addWidget(self.edit_process)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.lbl_resource)
        hbox2.addWidget(self.edit_resource)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.lbl_allocation)
        vbox.addWidget(self.edit_allocation)
        vbox.addWidget(self.lbl_max_need)
        vbox.addWidget(self.edit_max_need)
        vbox.addWidget(self.lbl_available)
        vbox.addWidget(self.edit_available)
        vbox.addWidget(self.btn_ok)
        vbox.addWidget(self.lbl_safe_sequences)
        vbox.addWidget(self.edit_safe_sequences)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 850, 1000)
        self.setWindowTitle("银行家算法")

        self.show()

    def on_click(self):
        n_process = int(self.edit_process.text())
        n_resource = int(self.edit_resource.text())
        allocation_array = self.edit_allocation.toPlainText()
        max_need_array = self.edit_max_need.toPlainText()
        available_resource_array = self.edit_available.toPlainText()

        safe_sequence = bankers(n_process, n_resource, allocation_array, max_need_array, available_resource_array)

        self.edit_safe_sequences.setText(safe_sequence)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UI()
    sys.exit(app.exec_())

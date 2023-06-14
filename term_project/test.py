from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem

app = QApplication([])
table_widget = QTableWidget(3, 2)  # 创建一个3x2的表格

# 设置第1行第2列单元格
item = QTableWidgetItem("Hello World")  # 创建一个QTableWidgetItem对象
item.setBackground(QColor(255, 0, 0))  # 设置背景色为红色
item.setForeground(QColor(255, 255, 255))  # 设置前景色为白色
table_widget.setItem(0, 1, item)  # 在第1行第2列位置设置该对象

table_widget.show()
app.exec_()



pt0 = 20
pt1 = 50
for i in range(10):
    for j in range(10):
        if pt0 > pt1:
            if (i*10+j < pt0 and i*10+j >= 0) or (i*10+j >= pt1 and i*10+j <= 99):
                self.spooling_pool0_input.item(i, j).setBackground(QColor(0, 255, 255))
            else:
                self.spooling_pool0_input.item(i, j).setBackground(QColor(0, 0, 0))
        else:
            if i*10+j >= pt0 and i*10+j < pt1:
                self.spooling_pool0_input.item(i, j).setBackground(QColor(0, 255, 255))
            else:
                self.spooling_pool0_input.item(i, j).setBackground(QColor(0, 0, 0))
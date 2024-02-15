from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
import css


app = QApplication([])
win_2 = QWidget()
win_2.resize(700,500)
win_2.setWindowTitle('/')

bt_1 = QPushButton('')
bt_2 = QPushButton('')


lb_image = QLabel('')

lb_image.setFixedSize(500,400)

v1 = QVBoxLayout()
v2 = QVBoxLayout()
h = QHBoxLayout()

v1.addWidget(bt_1)
v1.addWidget(bt_2)
v2.addWidget(lb_image)
def cat():
    pic=QPixmap("cat.jpg")
    pic=pic.scaled(500,400, Qt.KeepAspectRatio)
    lb_image.setPixmap(pic)
bt_1.clicked.connect(cat)
h.addLayout(v1)
h.addLayout(v2)

win_2.setLayout(h)

win_2.hide()

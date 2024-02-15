from PyQt5.QtWidgets import*
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from PyQt5.QtGui import QPixmap
import css
from win2 import *

app = QApplication([])
win = QWidget()
win.resize(700,500)
win.setWindowTitle('/')

btn_1 = QPushButton('тварини')
btn_2 = QPushButton('природа')
btn_3 = QPushButton('мебель')
btn_4 = QPushButton('фігури')
btn_5 = QPushButton('люди')
btn_6 = QPushButton('фантастика ')
btn_1.setStyleSheet(css.button)
btn_2.setStyleSheet(css.button)
btn_3.setStyleSheet(css.button)
btn_4.setStyleSheet(css.button)
btn_5.setStyleSheet(css.button)
btn_6.setStyleSheet(css.button)

h = QHBoxLayout()
v_1 = QVBoxLayout()
v_2 = QVBoxLayout()

v_1.addWidget(btn_1)
v_1.addWidget(btn_2)
v_1.addWidget(btn_3)

v_2.addWidget(btn_4)
v_2.addWidget(btn_5)
v_2.addWidget(btn_6)
h.addLayout(v_1)
h.addLayout(v_2)

win.setLayout(h)

def btn_1_click():
    bt_1.setText("котик")
    bt_2.setText("рибки")
    
    lb_image
    win_2.show()
    

btn_1.clicked.connect(btn_1_click)



win.show()
app.exec()
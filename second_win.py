from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QLabel

from instr import *
from final_win import *


class TestWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # створюємо та налаштовуємо графічні елементи
        self.connects()  # Встановлює зв'язки між елементами
        self.set_appear()  # Встановлює, як виглядатиме вікно (напис, розмір, місце)
        self.show()  # старт

    def set_appear(self):
        self.setWindowTitle("тест руфє")

    def initUI(self):
        lblname = QLabel(txt_name)
        lblage = QLabel(txt_age)
        lbl1 = QLabel(txt_test1)
        lbl2 = QLabel(txt_test2)
        lbl3 = QLabel(txt_test3)
        lbltimer = QLabel()
        self.editname = QLineEdit()
        self.editage = QLineEdit()
        self.edit1 = QLineEdit()
        self.edit2 = QLineEdit()
        self.edit3 = QLineEdit()
        self.btn1 = QPushButton(txt_starttest1)
        self.btn2 = QPushButton(txt_starttest2)
        self.btn3 = QPushButton(txt_starttest3)
        self.btn4 = QPushButton(txt_sendresults)
        V1 = QVBoxLayout()
        V2 = QVBoxLayout()
        H1 = QHBoxLayout()
        V1.addWidget(lblname,alignment=Qt.AlignLeft)
        V1.addWidget(self.editname,alignment=Qt.AlignLeft)
    
        V1.addWidget(lblage, alignment=Qt.AlignLeft)
        V1.addWidget(self.editage, alignment=Qt.AlignLeft)

        V1.addWidget(lbl1, alignment=Qt.AlignLeft)
        V1.addWidget(self.edit1, alignment=Qt.AlignLeft)
        V1.addWidget(self.btn1, alignment=Qt.AlignLeft)

        V1.addWidget(lbl2, alignment=Qt.AlignLeft)
        V1.addWidget(self.edit2, alignment=Qt.AlignLeft)
        V1.addWidget(self.btn2, alignment=Qt.AlignLeft)
        V1.addWidget(lbl3, alignment=Qt.AlignLeft)

        V1.addWidget(self.edit3, alignment=Qt.AlignLeft)
        V1.addWidget(self.btn3, alignment=Qt.AlignLeft)

        V1.addWidget(self.btn4, alignment=Qt.AlignCenter)
        V2.addWidget(lbltimer, alignment=Qt.AlignCenter)
        H1.addLayout(V1)
        H1.addLayout(V2)
        self.setLayout(H1)



    def next_click(self):
        self.hide()
        self.Final = FinalWin()
     

    def connects(self):
        self.btn4.clicked.connect(self.next_click)

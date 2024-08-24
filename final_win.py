from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel

from instr import *


class FinalWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # створюємо та налаштовуємо графічні елементи
        self.set_appear()  # Встановлює, як виглядатиме вікно (напис, розмір, місце)
        self.show()  # старт

    def set_appear(self):
        self.setWindowTitle("тест руфє")

    def initUI(self):
        lbl1 = QLabel(txt_index)
        lbl2 = QLabel(txt_workheart)
        layout = QVBoxLayout()
        layout.addWidget(lbl1)
        layout.addWidget(lbl2)
        self.setLayout(layout)

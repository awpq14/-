from second_win import *
from instr import *
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout


class MainWin(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()  # створюємо та налаштовуємо графічні елементи
        self.connects()  # Встановлює зв'язки між елементами
        self.set_appear()  # Встановлює, як виглядатиме вікно (напис, розмір, місце)
        self.show()  # старт

    def set_appear(self):
        ...

    def initUI(self):
        ...

    def connects(self):
        ...

    def next_click(self):
        ...


app = QApplication([])
mw = MainWin()
app.exec_()

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
        self.setWindowTitle("тест руфє")

    def initUI(self):
        lbl1 = QLabel(txt_hello)
        lbl2 = QLabel(txt_instruction)
        self.btn = QPushButton(txt_next)
        layout = QVBoxLayout()
        layout.addWidget(lbl1)
        layout.addWidget(lbl2)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def connects(self):
        self.btn.clicked.connect(self.next_click)

    def next_click(self):
        self.hide()
        test = TestWin()


app = QApplication([])
mw = MainWin()
app.exec_()

import sys
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import random


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.label = None
        f = "UI.ui"
        self.setWindowTitle("Circles")
        uic.loadUi(f, self)
        self.pushButton.clicked.connect(self.DrawCirles)
        self.circles = list()
        self.setGeometry(60, 60, 600, 400)

    def DrawCirles(self):
        self.label = QLabel(self)
        a = random.randint(10, 100)
        x = random.randint(0, self.width() - a)
        y = random.randint(0, self.height() - a)
        self.label.move(x, y)
        self.label.resize(a, a)
        self.label.setStyleSheet(f"border: 3px solid yellow; border-radius: {a // 2}px;")
        self.label.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    ex.show()
    sys.exit(app.exec_())

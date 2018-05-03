import sys
from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow



class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Window Title"
        self.top = 0
        self.left = 0
        self.width = 500
        self.height = 500

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())


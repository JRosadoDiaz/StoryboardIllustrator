from PyQt5.QtWidgets import QMainWindow, QApplication
from Models.PropertiesMenuModel import PropertiesMenu

import sys


class TestWindow(QMainWindow):
    windowSize = (400, 900)

    def __init__(self):
        super(TestWindow, self).__init__()

        self.resize(self.windowSize[0], self.windowSize[1])
        self.setWindowTitle("Properties Menu")

        menu = PropertiesMenu()
        self.addWidget(menu)

    def addWidget(self, widget):
        self.setCentralWidget(widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = TestWindow()
    win.show()
    app.exec_()

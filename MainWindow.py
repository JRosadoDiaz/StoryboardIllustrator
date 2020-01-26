from PyQt5.QtWidgets import QMainWindow, QApplication
from Models.Storyboard import Storyboard

import sys


class MainWindow(QMainWindow):
    windowSize = (1600, 900)

    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(self.windowSize[0], self.windowSize[1])
        self.setWindowTitle("Hello")

        board = Storyboard()
        self.setCentralWidget(board)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

from PyQt5.QtWidgets import (QMainWindow, QApplication, QPushButton, QAction,
                             qApp)
from StartupWidget import StartupWidget

import sys


class StartupWindow(QMainWindow):
    windowSize = (1600, 900)

    def __init__(self):
        super(StartupWindow, self).__init__()
        self.resize(self.windowSize[0], self.windowSize[1])
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Storyboard Illustrator")

        self.wid = StartupWidget()
        self.setCentralWidget(self.wid)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = StartupWindow()
    win.show()
    app.exec_()

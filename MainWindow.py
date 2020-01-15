from PyQt5.QtWidgets import QMainWindow, QApplication
from Models.Storyboard import Storyboard

# , Panel
import sys


class MainWindow(QMainWindow):
    windowSize = [1600, 900]

    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(self.windowSize[0], self.windowSize[1])
        self.setWindowTitle("Hello")

        board = Storyboard()
        self.addWidget(board)

    def addWidget(self, widget):
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
dialog = MainWindow()
dialog.show()
app.exec_()

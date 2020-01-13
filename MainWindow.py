from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel
import sys


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Hello")

        self.label = QLabel("Hello World")

        self.setCentralWidget(self.label)


app = QApplication(sys.argv)
dialog = MainWindow()
dialog.show()
app.exec_()

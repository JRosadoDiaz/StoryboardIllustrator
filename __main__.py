from PyQt5.QtWidgets import QApplication
import sys
from StartupWindow import StartupWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = StartupWindow()
    win.show()
    app.exec_()
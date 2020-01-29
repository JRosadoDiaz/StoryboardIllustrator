from PyQt5.QtWidgets import QMainWindow, QApplication, QDockWidget
from PyQt5.QtCore import Qt
from Models.Storyboard import Storyboard
from Models.PropertiesMenuModel import PropertiesMenu

import sys


class MainWindow(QMainWindow):
    windowSize = (1600, 900)

    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(self.windowSize[0], self.windowSize[1])
        self.setWindowTitle("Hello")

        # Build Properties menu
        propertiesMenu = QDockWidget('Properties', self)
        menu = PropertiesMenu()
        propertiesMenu.setWidget(menu)
        propertiesMenu.setFloating(False)

        board = Storyboard()
        board.newPanelSignal.connect(menu.panelChanged)
        self.setCentralWidget(board)

        self.addDockWidget(Qt.RightDockWidgetArea, propertiesMenu)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

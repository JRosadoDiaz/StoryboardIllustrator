from PyQt5.QtWidgets import QMainWindow, QApplication, QDockWidget
from PyQt5.QtCore import Qt
from Models.Storyboard import Storyboard
from Models.PropertiesMenuModel import PropertiesMenu

import sys


class MainWindow(QMainWindow):
    windowSize = (1900, 1600)
    propertiesMenuOpen = False

    def __init__(self):
        super(MainWindow, self).__init__()

        self.resize(self.windowSize[0], self.windowSize[1])
        self.setWindowTitle("Storyboard Illustrator")

        board = Storyboard()

        # Build Properties menu
        menu = PropertiesMenu()
        propertiesDock = QDockWidget('Properties', self)
        propertiesDock.setMinimumWidth(500)
        propertiesDock.setWidget(menu)
        propertiesDock.setFloating(False)

        board.newPanelSignal.connect(menu.panelChanged)
        menu.deleteSignal.connect(board.deletePanel)

        self.setCentralWidget(board)
        self.addDockWidget(Qt.RightDockWidgetArea, propertiesDock)

    def openPropertiesMenu(self):
        if(self.propertiesMenuOpen is False):
            self.propertiesMenuOpen = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

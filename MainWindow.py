from PyQt5.QtWidgets import (QMainWindow, QApplication, QDockWidget, QAction,
                             qApp)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from Models.Storyboard import Storyboard
from Models.PropertiesMenuModel import PropertiesMenu

import sys


class MainWindow(QMainWindow):
    windowSize = (3200, 1900)
    propertiesMenuOpen = False
    panelSelected = False
    projectUpToDate = True  # False whenever panel is updated

    def __init__(self, file=None, panelCount=1):
        super(MainWindow, self).__init__()
        self.resize(self.windowSize[0], self.windowSize[1])
        self.initUI(file)

    def initUI(self, file):

        # Build components
        
        self.board = Storyboard(file)
        propDock = self.buildPropMenu()

        # Connect signals from storyboard and menus
        self.board.newPanelSignal.connect(self.menu.panelChanged)
        self.board.newPanelSignal.connect(self.panelSelected)
        self.menu.deleteSignal.connect(self.board.deletePanel)

        # self.statusBar().showMessage('Ready')

        self.buildMenuBar()
        self.setCentralWidget(self.board)
        self.addDockWidget(Qt.RightDockWidgetArea, propDock)

    def buildMenuBar(self):
        """Builds menu bar on top of screen"""

        menuBar = self.menuBar()

        # File
        fileMenu = menuBar.addMenu('&File')

        # File -> New Project

        # File -> Open Project

        # File -> Save Project
        saveAct = QAction('&Save Project', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('Save Project')
        saveAct.triggered.connect(self.board.serializeBoard)

        fileMenu.addAction(saveAct)

        # File -> Save Project as

        # File -> Convert to image

        # File -> Exit
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit Application')
        exitAct.triggered.connect(qApp.quit)

        fileMenu.addAction(exitAct)

        # Panel
        panelMenu = menuBar.addMenu('&Panel')

        # Panel -> New Panel
        newPanelAct = QAction(QIcon(''), '&New Panel', self)
        newPanelAct.setShortcut('Ctrl+N')
        newPanelAct.setStatusTip('Add blank panel')
        newPanelAct.triggered.connect(self.board.addPanel)

        panelMenu.addAction(newPanelAct)

        # Panel -> Delete Panel *Only activate if a panel is selected*
        self.deletePanelAct = QAction(QIcon(''), '&Delete Panel', self)
        self.deletePanelAct.setStatusTip('Delete selected panel')
        self.deletePanelAct.setEnabled = False
        self.deletePanelAct.triggered.connect(self.board.deletePanel)

        panelMenu.addAction(self.deletePanelAct)

        # View
        # viewMenu = menuBar.addMenu('&View')

        # View -> Tool Menu

        # View -> Panel Properties

        # Help
        helpMenu = menuBar.addMenu('&Help')

        # Help -> About
        helpAct = QAction('&About', self)
        helpAct.triggered.connect(self.displayHelpDialog)

        helpMenu.addAction(helpAct)

    def displayHelpDialog(self):
        print("help is displayed")

    def panelSelected(self):
        self.deletePanelAct.setEnabled = True

    def buildPropMenu(self):
        self.menu = PropertiesMenu()
        propertiesDock = QDockWidget('Properties', self)
        propertiesDock.setMinimumWidth(500)
        propertiesDock.setWidget(self.menu)
        propertiesDock.setFloating(False)

        return propertiesDock

    def openPropertiesMenu(self):
        if(self.propertiesMenuOpen is False):
            self.propertiesMenuOpen = True


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec_()

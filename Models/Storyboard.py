# from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QGridLayout, QGroupBox, QVBoxLayout,
                             QLabel)


class Storyboard(QWidget):
    panels = []
    # panelSelected = None

    def __init__(self):
        super(Storyboard, self).__init__()

        grid = QGridLayout()
        grid.addWidget(self.CreatePanel(), 0, 0)
        self.setLayout(grid)

    def CreatePanel(self):
        groupBox = QGroupBox("Panel")
        vbox = QVBoxLayout()
        label = QLabel("Hello")
        vbox.addWidget(label)
        groupBox.setLayout(vbox)
        return groupBox

    def ReadPanel(self, panel):
        pass

    def UpdatePanel(self, panel):
        pass

    def DeletePanel(self, panelSelected):
        pass

    def SerializeBoard(self):
        pass

    def DeserializeBoard(self):
        pass

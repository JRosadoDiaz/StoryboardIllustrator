# from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QGridLayout

# , QGroupBox, QVBoxLayout,
# QLabel)
from . import PanelModel
# from PanelModel import Panel


class Storyboard(QWidget):
    panels = []
    # panelSelected = None

    def __init__(self):
        super(Storyboard, self).__init__()

        grid = QGridLayout()

        # Read through file for all panels and generate a list
        # Use list and build all panels accordingly

        grid.addWidget(self.CreatePanel(), 0, 0)
        # grid.addWidget(self.CreatePanel(), 0, 1)
        # grid.addWidget(self.CreatePanel(), 0, 2)

        # Prepare layout with all panels
        self.setLayout(grid)

    def CreatePanel(self):
        p = PanelModel.Panel(1, "Hello")
        self.panels.append(p)
        print("storyboard created a panel")
        return p.buildComponents()

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

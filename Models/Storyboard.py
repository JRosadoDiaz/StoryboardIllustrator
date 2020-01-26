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
        """Creates a panel and adds it to the storyboard list"""
        p = PanelModel.Panel(1, "Hello")
        self.panels.append(p)
        panelBox = p.buildComponents()
        print("storyboard created a panel")
        return panelBox

    def ReadPanel(self, panelData):
        """Reads data from file and builds individual panel"""
        pass

    def UpdatePanel(self, panel):
        """
        for x in self.panels:
            if x == panel:
                # Take new values and replace with old
                # must replace:
                # Panel text
                # Panel image
                break
        """

    def DeletePanel(self, panelSelected):
        """Deletes panel given from list and update board"""
        pass

    def SerializeBoard(self):
        pass

    def DeserializeBoard(self):
        pass

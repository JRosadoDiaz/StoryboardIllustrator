from PyQt5.QtWidgets import QWidget, QGridLayout
from . import PanelModel
# from PanelModel import Panel


class Storyboard(QWidget):
    panels = []
    panelSelected = None

    def __init__(self):
        super(Storyboard, self).__init__()

        grid = QGridLayout()

        # Read through file for all panels and generate a list
        # Use list and build all panels accordingly

        grid.addWidget(self.CreatePanel(1), 0, 0)
        grid.addWidget(self.CreatePanel(2), 0, 1)
        # grid.addWidget(self.CreatePanel(), 0, 2)

        # Prepare layout with all panels

        self.setLayout(grid)

    def CreatePanel(self, id):
        """Creates a panel and adds it to the storyboard list"""
        p = PanelModel.Panel(id, "Hello")
        self.panels.append(p)
        p.clicked.connect(self.SetSelectedPanel)
        print("storyboard created a panel")
        return p

    def SetSelectedPanel(self, panel):
        """Update selected panel with the one given"""

        print(f"Id: {panel.panelId}, Text: {panel.text}")
        # print(f"text: {panel[1]}")
        for x in self.panels:
            if (x.panelId == panel.panelId):
                # print(f"Panel {panel.panelId} was found within {x.panelId}")

                # Update values within panel
                x.text = panel.text

                # print(f"panel in storyboard list now has {x.text}")

                self.panelSelected = x
        # print(f"Selected Panel has changed to {self.panelSelected.panelId}")
        # print(f"Its contents contain {self.panelSelected.text}")

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

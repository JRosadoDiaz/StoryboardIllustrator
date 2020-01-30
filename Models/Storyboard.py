from PyQt5.QtWidgets import QWidget, QGridLayout
from PyQt5.QtCore import pyqtSignal
from . import PanelModel
# from PanelModel import Panel


class Storyboard(QWidget):
    panels = []
    selectedPanel = None
    newPanelSignal = pyqtSignal(object)

    def __init__(self):
        super(Storyboard, self).__init__()

        grid = QGridLayout()

        # Read through file for all panels and generate a list
        # Use list and build all panels accordingly

        grid.addWidget(self.createPanel(1), 0, 0)
        grid.addWidget(self.createPanel(2), 0, 1)
        grid.addWidget(self.createPanel(3), 0, 2)
        grid.addWidget(self.createPanel(1), 1, 0)
        grid.addWidget(self.createPanel(2), 1, 1)
        grid.addWidget(self.createPanel(3), 1, 2)


        # Prepare layout with all panels
        self.setLayout(grid)

        self.installEventFilter(self)

    def createPanel(self, id):
        """Creates a panel and adds it to the storyboard list"""
        p = PanelModel.Panel(id, "Hello")
        self.panels.append(p)
        p.clicked.connect(self.setSelectedPanel)
        print("storyboard created a panel")
        return p

    def setSelectedPanel(self, panel):
        """Update selected panel with the one given"""

        print(f"Id: {panel.panelId}, Text: {panel.text}")
        # print(f"text: {panel[1]}")
        for x in self.panels:
            if (x.panelId == panel.panelId):
                # print(f"Panel {panel.panelId} was found within {x.panelId}")

                # Update values within panel
                x.text = panel.text

                # print(f"panel in storyboard list now has {x.text}")

                self.selectedPanel = x
                self.newPanelSignal.emit(self.selectedPanel)

    def readPanel(self, panelData):
        """Reads data from file and builds individual panel"""
        pass

    def updatePanel(self, panel):
        """
        for x in self.panels:
            if x == panel:
                # Take new values and replace with old
                # must replace:
                # Panel text
                # Panel image
                break
        """

    def deletePanel(self, panelSelected):
        """Deletes panel given from list and update board"""
        pass

    def serializeBoard(self):
        pass

    def deserializeBoard(self):
        pass

from PyQt5.QtWidgets import QWidget, QGridLayout, QPushButton
from PyQt5.QtCore import pyqtSignal
from . import PanelModel
# from PanelModel import Panel


class Storyboard(QWidget):
    panelCount = 0
    panels = []
    selectedPanel = None
    newPanelSignal = pyqtSignal(object)

    def __init__(self):
        super(Storyboard, self).__init__()

        # Read through file for all panels and generate a list
        # Use list and build all panels accordingly

        # Test values
        self.panels = [self.createNewPanel(1), self.createNewPanel(2),
                       self.createNewPanel(3), self.createNewPanel(4)]
        print(len(self.panels))
        self.panelCount = 4
        ########

        self.grid = QGridLayout()
        self.buildBoard_Test(self.panels)

        # Prepare layout with all panels
        self.setLayout(self.grid)

        self.installEventFilter(self)

    def buildBoard_Test(self, tempList):
        """
        Takes list of panels to be built onto grid. Adds new button on end
        """

        # Create a counter of rows and columns upon each new panel
        row = 0
        column = 0

        # Check if we have at least one panel
        if(self.panelCount >= 1):
            # Each panel gets built onto another panel
            counter = 1
            for x in tempList:
                x.panelId = counter
                newPanel = self.createNewPanel(x.panelId, x.text)
                self.grid.addWidget(newPanel, column, row)

                counter += 1

                # updated after placing a panel to prep for last button
                row += 1
                if(row == 3):
                    row = 0
                    column += 1

            # Once all panels are added, place new panel button on the end
            newPanelButton = QPushButton("New")
            newPanelButton.clicked.connect(self.addPanel)
            self.grid.addWidget(newPanelButton, column, row)

    def createNewPanel(self, id, text='Test'):
        """Creates a panel with click functionality and returns it"""
        p = PanelModel.Panel(id, text)
        p.resize(900, 900)
        p.clicked.connect(self.setSelectedPanel)
        return p

    def addPanel(self):
        """Adds new empty panel to end of list"""

        self.clearGrid()

        # Create new panel
        newPanel = self.createNewPanel(self.panelCount + 1, '')
        # Add new panel to panels list and add to counter
        self.panels.append(newPanel)
        self.panelCount += 1
        # Clear then rebuild grid with updated list
        self.buildBoard_Test(self.panels)

        print("New panel is added")

    def deletePanel(self):
        """Deletes panel given from list and update board"""

        # Checks if there is at least one panel
        if(self.panelCount > 1):
            # Delete all widgets including new button panel
            self.clearGrid()

            # delete panel from list
            # Replace later with panelSelected
            self.panels.remove(self.panels[0])
            self.panelCount -= 1

            # rebuild grid with new list without removed panel
            tempList = self.panels.copy()
            self.panels.clear()  # Clears panel list to be rebuilt
            self.buildBoard_Test(tempList)

            for x in tempList:
                self.panels.append(x)

            print(self.panelCount)
        else:
            print(f"Only {len(self.panels)} remains, delete aborted")

    def clearGrid(self):
        """Clears grid of all elements"""
        for x in range(self.grid.count()):
            self.grid.itemAt(x).widget().deleteLater()
        
        print("Grid was emptied")

    def setSelectedPanel(self, panel):
        """Update selected panel with the one given"""

        print(f"Id: {panel.panelId}, Text: {panel.text}")
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

    def serializeBoard(self):
        pass

    def deserializeBoard(self):
        pass

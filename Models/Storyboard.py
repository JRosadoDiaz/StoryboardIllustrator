from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QScrollArea,
                             QGroupBox, QVBoxLayout)
from PyQt5.QtCore import pyqtSignal
from . import PanelModel


class Storyboard(QWidget):
    panelCount = 0  # Panel count is to create initial panels upon launch
    panelMasterList = []  # The master list of all panels
    selectedPanel = None  # Whenever a panel is clicked, this gets updated
    newPanelSignal = pyqtSignal(object)

    def __init__(self, file=None, count=1):
        super(Storyboard, self).__init__()
        self.panelCount = count

        # Read through file for all panels and generate a list
        # Use list and build all panels accordingly
        if file is not None:
            self.deserializeBoard(file)
        else:
            # No file was given, create blank panels
            for i in range(count):
                self.panelMasterList.append(self.createNewPanel(i + 1))

        self.buildStoryboardView()

    def buildStoryboardView(self):
        '''Builds the main components for the storyboard window'''

        # We put the panels within a groupbox
        # The groupbox becomes added into a scroll area
        # https://www.youtube.com/watch?v=TXZkHy2koyo
        self.panelGroupBox = QGroupBox()
        self.panelGrid = QGridLayout()

        # First a copy of the main list of panels are created and sent
        # to the board
        self.rebuildBoard()
        self.panelGroupBox.setLayout(self.panelGrid)

        # Create scroll area and put groupbox inside it
        scroll = QScrollArea()
        scroll.setWidget(self.panelGroupBox)
        scroll.setWidgetResizable(True)

        # put scroll into a layout to add to main widget
        widgetLayout = QVBoxLayout()
        widgetLayout.addWidget(scroll)
        self.setLayout(widgetLayout)

        self.installEventFilter(self)

    def buildBoard(self, panelList):
        '''Builds the layout that contains all panels.
        Is used to both initialize board and update'''

        # Create a counter of rows and columns upon each new panel
        row = 0
        column = 0

        # Check if we have at least one panel
        if(self.panelCount >= 1):
            counter = 1
            for x in panelList:
                x.panelId = counter
                self.panelGrid.addWidget(x, column, row)

                counter += 1

                # updated after placing a panel to prep for last button
                row += 1
                if(row == 3):
                    row = 0
                    column += 1

            # Once all panels are added, place new panel button on the end
            newPanelButton = QPushButton("New")
            newPanelButton.clicked.connect(self.addPanel)
            self.panelGrid.addWidget(newPanelButton, column, row)

    def rebuildBoard(self):
        '''Creates a new copy of panelMasterList to rebuild board'''
        print("Rebuilding board")
        tempList = []
        for x in self.panelMasterList:
            if(type(x) == PanelModel.Panel):
                p = PanelModel.Panel(x.panelId, x.text)
                p.canvas.image = x.canvas.image.copy()
                tempList.append(p)

        self.buildBoard(tempList)

    def createNewPanel(self, id, text=''):
        """Creates a panel and returns it"""
        p = PanelModel.Panel(id, text)
        p.resize(900, 900)
        p.clicked.connect(self.setSelectedPanel)
        p.panelEdited.connect(self.updatePanel)
        return p

    def addPanel(self):
        '''Clears the grid to add another blank panel'''
        self.clearGrid()

        # Create new panel then add to list, increment counter
        newPanel = self.createNewPanel(self.panelCount + 1, '')
        self.panelMasterList.append(newPanel)
        self.panelCount += 1
        self.rebuildBoard()

        print("New panel is added")

    def updatePanel(self, panel):
        """Takes information from given panel and updates it on the list"""

        for x in self.panelMasterList:
            if x.panelId == panel.panelId:
                print("Panel Found and updated")
                x = panel
                break

    def updatePanelFromList(self, list):
        """Updates panel from a given list"""
        for x in self.panelMasterList:
            if x.panelId == list[0]:
                print("Panel Found!")

    def deletePanel(self):
        """Deletes panel given from list and update board"""
        # Checks if there is at least one panel
        if(self.panelCount > 1):
            # Delete all widgets including new button panel
            self.clearGrid()

            # delete panel from list
            # Replace later with panelSelected
            self.panelMasterList.remove(self.panelMasterList[0])
            """
            for x in self.panelMasterList:
                if self.selectedPanel.panelId == x.panelId:
                    self.panelMasterList.remove(self.panelMasterList[x])
                    break
            """

            self.panelCount -= 1

            # rebuild panelGrid with new list without removed panel
            self.rebuildBoard()

            print("panel deleted")
        else:
            print(f"Only {len(self.panelMasterList)} remains, delete aborted")

    def clearGrid(self):
        """Clears panelGrid of all elements"""

        for x in range(self.panelGrid.count()):
            if type(self.panelGrid.itemAt(x).widget()) == PanelModel.Panel:
                self.panelMasterList[x].text = self.panelGrid.itemAt(x).widget().text

                self.panelMasterList[x].canvas.image = self.panelGrid.itemAt(x).widget().canvas.image.copy()

            self.panelGrid.itemAt(x).widget().deleteLater()

        print("Grid was emptied")

    def setSelectedPanel(self, panel):
        """Update selected panel with the one given"""

        print(f"Id: {panel.panelId}, Text: {panel.text}")
        for x in self.panelMasterList:
            if (x.panelId == panel.panelId):
                # Update values within panel
                x.canvas = panel.canvas
                x.text = panel.text

                self.selectedPanel = x
                self.newPanelSignal.emit(self.selectedPanel)

    def readPanel(self, panelData):
        """Reads data from file and builds individual panel"""
        pass

    def updatePanelImage(self, img):
        print(self.panelMasterList[0].text)

    def serializeBoard(self):
        """Calls serialize function on all panels to create a single file"""

        for p in self.panelMasterList:
            print(p.text)

        self.panelMasterList[0].canvas.saveImage('./Models/image.png', "PNG")

    def deserializeBoard(self, file):
        """Reads a given file and builds board accoringly"""
        pass

from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QScrollArea,
                             QGroupBox, QVBoxLayout)
from PyQt5.QtCore import pyqtSignal
from . import PanelModel


class Storyboard(QWidget):
    panelCount = 0
    panels = []
    selectedPanel = None
    newPanelSignal = pyqtSignal(object)

    def __init__(self, file=None, panelCount=1):
        super(Storyboard, self).__init__()
        self.panelCount = panelCount

        # Read through file for all panels and generate a list
        # Use list and build all panels accordingly
        if file is not None:
            self.deserializeBoard(file)
        else:
            # No file was given, create blank panels
            for i in range(panelCount):
                self.panels.append(self.createNewPanel(1))
                print("Upon launching there is " +
                      str(len(self.panels)) + " panel(s)")

        # We put the panels within a groupbox
        # The groupbox becomes added into a scroll area
        # https://www.youtube.com/watch?v=TXZkHy2koyo
        self.panelGroupBox = QGroupBox()
        self.panelGrid = QGridLayout()

        # Panels are created and then updated in here
        self.buildBoard(self.panels)
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
                newPanel = self.createNewPanel(x.panelId, x.text)
                self.panelGrid.addWidget(newPanel, column, row)

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
        # Clear then rebuild panelGrid with updated list
        self.buildBoard(self.panels)

        print("New panel is added")

    def deletePanel(self):
        """Deletes panel given from list and update board"""
        print(self.panelCount)
        # Checks if there is at least one panel
        if(self.panelCount > 1):
            # Delete all widgets including new button panel
            self.clearGrid()

            # delete panel from list
            # Replace later with panelSelected
            self.panels.remove(self.panels[0])
            self.panelCount -= 1

            # rebuild panelGrid with new list without removed panel
            tempList = self.panels.copy()
            self.panels.clear()  # Clears panel list to be rebuilt
            self.buildBoard(tempList)

            for x in tempList:
                self.panels.append(x)

            print(self.panelCount)
        else:
            print(f"Only {len(self.panels)} remains, delete aborted")

    def clearGrid(self):
        """Clears panelGrid of all elements"""
        for x in range(self.panelGrid.count()):
            self.panelGrid.itemAt(x).widget().deleteLater()

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

    def updatePanelImage(self, img):
        print(self.panels[0].text)

    def updatePanel(self, panel):
        """Takes information from given panel and updates it on the list"""
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
        """Calls serialize function on all panels to create a single file"""

        """
        file = ???
        for x in self.panels:
            x.serialize()

        return file
        """
        # self.panels[0].canvas.image.save('./Models/' + 'test.png')
        # self.panels[0].canvas.image.save('./Models/' + 'test.png')

        # self.panels[0].serialize()

        self.panels[0].canvas.saveImage('./Models/image.png', "PNG")

    def deserializeBoard(self, file):
        """Reads a given file and builds board accoringly"""
        pass

from PyQt5.QtWidgets import (QWidget, QGridLayout, QVBoxLayout, QPushButton,
                             QLabel, QLineEdit, QFileDialog, QGroupBox)
from PyQt5.Qt import pyqtSignal


class MainMenu(QWidget):

    newProjectButtonClicked = pyqtSignal(int)

    def __init__(self):
        super(MainMenu, self).__init__()

        self.buildComponents()

    def buildComponents(self):
        layout = QVBoxLayout()

        # Build components
        self.newProjectButton = QPushButton("New Project")
        self.newProjectButton.clicked.connect(self.newProjectSettingsOpen)

        self.loadProjectButton = QPushButton("Load Project")

        layout.addWidget(self.newProjectButton)
        layout.addWidget(self.loadProjectButton)

        self.setLayout(layout)

    def newProjectSettingsOpen(self):
        self.newProjectButtonClicked.emit(1)


class NewProjectSettingsWidget(QWidget):

    backButtonClicked = pyqtSignal(int)
    startProjectClicked = pyqtSignal(object)

    def __init__(self):
        super(NewProjectSettingsWidget, self).__init__()

        self.buildComponents()

    def buildComponents(self):
        '''Builds components for main new project view'''
        layout = QGridLayout()

        # Build components
        # Project name
        nameGroup = QGroupBox()
        nameLayout = QVBoxLayout()
        projectNameLabel = QLabel("Project Name:")
        projectNameLineEdit = QLineEdit()
        nameLayout.addWidget(projectNameLabel)
        nameLayout.addWidget(projectNameLineEdit)
        nameGroup.setLayout(nameLayout)
        layout.addWidget(nameGroup, 0, 1)

        # File Location
        fileGroup = QGroupBox()
        fileLayout = QGridLayout()
        fileLocationLabel = QLabel("File Location:")
        fileLocationLineEdit = QLineEdit()
        fileLocationButton = QPushButton("Browse")
        fileLocationButton.clicked.connect(self.openFileDialog)
        fileLayout.addWidget(fileLocationLabel, 0, 0)
        fileLayout.addWidget(fileLocationLineEdit, 1, 0)
        fileLayout.addWidget(fileLocationButton, 1, 1)
        fileGroup.setLayout(fileLayout)
        layout.addWidget(fileGroup, 1, 1)

        # Back button
        backButton = QPushButton("Back")
        backButton.clicked.connect(self.backButton)
        layout.addWidget(backButton, 3, 0)

        # Start button
        startProjectButton = QPushButton("Start Project")
        startProjectButton.clicked.connect(self.openStoryboardWindow)
        layout.addWidget(startProjectButton, 3, 2)

        # https://stackoverflow.com/questions/21824772/qt-empty-space-column-in-qgridlayout
        # By using replacing column with rows, the spacing can be manipulated easily
        layout.setRowStretch(2, 1)

        self.setLayout(layout)

    def backButton(self):
        '''Emits a signal indicating to switch to the main menu'''
        self.backButtonClicked.emit(2)

    def openStoryboardWindow(self):
        '''Opens the storyboard window with given settings'''
        self.startProjectClicked.emit(projectSettings())

    def openFileDialog(self):
        '''Open the file dialog window to select file location'''
        pass
        '''
        fileName = QFileDialog.getOpenFileName(self, 'Open File')

        if fileName[0]:
            f = open(fileName[0], 'r')

            with 
        '''


class projectSettings:

    projectTitle = ''
    panelCount = 1
    
    def __init__(self, title='Test Title', count=1):
        self.panelCount = count
        self.projectTitle = title
        


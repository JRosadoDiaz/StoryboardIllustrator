from PyQt5.QtWidgets import (QWidget, QLabel,
                             QPlainTextEdit, QGridLayout)
from PyQt5.QtCore import QEvent, pyqtSignal, Qt
from Models.PanelCanvas import Canvas


class Panel(QWidget):

    # When clicked, this signal will emit an object that we give it
    clicked = pyqtSignal(object)

    panelId = None
    text = None
    canvas = None
    imgBoxSize = (800, 500)
    descriptionBoxSize = (800, 200)

    def __init__(self, id, panelText=""):
        super(Panel, self).__init__()
        self.panelId = id
        self.text = panelText

        self.installEventFilter(self)
        self.setLayout(self.buildComponents())

    def eventFilter(self, obj, event):
        """Emits itself to storyboard to indicate it is currently selected"""
        if isinstance(obj, (Panel, QPlainTextEdit,
                      Canvas)) and event.type() == QEvent.MouseButtonPress:
            print(f"Panel {self.panelId} was clicked")
            self.clicked.emit(self)

        return QWidget.eventFilter(self, obj, event)

    def buildComponents(self):
        """Builds components for Panel. Returns QGroupBox widget"""
        panelGrid = QGridLayout()

        # Content box
        self.canvas = self.createCanvas()
        self.imgWidget = self.canvas
        self.imgWidget.setFixedSize(800, 500)

        # Description box
        self.descriptionText = QPlainTextEdit(self.text)
        # textEdited fires when the user makes a change
        self.descriptionText.textChanged.connect(self.updateField)
        self.descriptionText.setFixedSize(800, 300)

        # Panel Id
        self.panelIdLabel = QLabel(str(self.panelId))
        self.panelIdLabel.setAlignment(Qt.AlignCenter)

        # Add widgets to grid
        panelGrid.addWidget(self.imgWidget, 0, 0)
        panelGrid.addWidget(self.descriptionText, 1, 0)
        panelGrid.addWidget(self.panelIdLabel, 2, 0)

        return panelGrid

    def createCanvas(self):
        return Canvas()

    def updateField(self):
        """Updates the saved text from description text box"""
        self.text = self.descriptionText.toPlainText()
        print(self.text)

    def getId(self):
        return self.panelId

    def serialize(self):
        pass

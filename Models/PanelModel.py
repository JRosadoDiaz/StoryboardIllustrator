from PyQt5.QtWidgets import (QWidget, QLabel,
                             QPlainTextEdit, QGridLayout)
from PyQt5.QtCore import (QEvent, pyqtSignal, Qt, QByteArray, QBuffer)
from Models.Widgets.PanelCanvas import Canvas


class Panel(QWidget):

    # When clicked, this signal will emit an object that we give it
    clicked = pyqtSignal(object)
    panelEdited = pyqtSignal(object)

    imgBoxSize = (800, 500)
    descriptionBoxSize = (800, 200)

    def __init__(self, id, panelText=""):
        super(Panel, self).__init__()
        self.panelId = id
        self.text = panelText
        self.canvas = None

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
        panelGrid.setRowStretch(3, 1)

        # Content box
        self.canvas = Canvas()
        self.canvas.setFixedSize(800, 500)
        self.canvas.released.connect(self.canvasEdited)

        # Description box
        self.descriptionText = QPlainTextEdit(self.text)
        self.descriptionText.placeholderText = "Insert panel description here."
        self.descriptionText.setFixedSize(800, 300)
        self.descriptionText.textChanged.connect(self.updateField)

        # Panel Id
        self.panelIdLabel = QLabel(str(self.panelId))
        self.panelIdLabel.setAlignment(Qt.AlignCenter)

        # Add widgets to grid
        panelGrid.addWidget(self.canvas, 0, 0)
        panelGrid.addWidget(self.descriptionText, 1, 0)
        panelGrid.addWidget(self.panelIdLabel, 2, 0)

        return panelGrid

    def canvasEdited(self, img):
        '''Updates canvas before emitting itself to be updated'''
        self.canvas.image = img
        self.panelEdited.emit(self)

    def updateField(self):
        """Updates the saved text from description text box"""
        self.text = self.descriptionText.toPlainText()
        self.panelEdited.emit(self)

    def getId(self):
        """Returns panel id"""
        return self.panelId

    def serialize(self):
        pass

    def deserialize(self, bArray):
        # convert bytes to QPixmap
        pixmap_bytes = bArray.data()
        ba = QByteArray(pixmap_bytes)
        ok = self.canvas.image.loadFromData(ba, "PNG")
        assert ok
        print(type(self.canvas.image))

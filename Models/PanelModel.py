from PyQt5.QtWidgets import (QWidget, QLabel,
                             QPlainTextEdit, QGridLayout)
from PyQt5.QtCore import (QEvent, pyqtSignal, Qt, QByteArray, QBuffer,
                          QIODevice)
# from PyQt5.QtGui import QPixmap
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
        self.imgWidget.released.connect(self.canvasEdited)

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

    def canvasEdited(self, img):
        self.canvas.image = img
        print('image updated')

    def createCanvas(self):
        return Canvas()

    def updateField(self):
        """Updates the saved text from description text box"""
        self.text = self.descriptionText.toPlainText()
        print(self.text)

    def getId(self):
        return self.panelId

    def serialize(self):
        # Convert canvas image to byte array
        pixmap = self.canvas.image

        # convert QPixmap to bytes
        ba = QByteArray()
        buff = QBuffer(ba)
        buff.open(QIODevice.WriteOnly)
        ok = pixmap.save(buff, "PNG")
        assert ok
        pixmap_bytes = ba.data()
        print(type(pixmap_bytes))
        print(len(pixmap_bytes))  # Size returns 2358
        return pixmap_bytes

    def deserialize(self, bArray):
        # convert bytes to QPixmap
        pixmap_bytes = bArray.data()
        ba = QByteArray(pixmap_bytes)
        ok = self.canvas.image.loadFromData(ba, "PNG")
        assert ok
        print(type(self.canvas.image))

from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QLabel, QGroupBox,
                             QPlainTextEdit)
from PyQt5.QtGui import QPixmap


class Panel(QWidget):

    panelId = None
    text = None
    img = 'barn-clipart-vector-25.png'

    def __init__(self, id, panelText=""):
        print("Panel model has been created")

        self.panelId = id
        self.text = panelText
        super(Panel, self).__init__()

    def buildComponents(self):
        groupBox = QGroupBox("Panel")
        vbox = QVBoxLayout()

        """
        Content box
            contains either the canvas drawing or
            the image file uploaded by user
        """

        contentBox = QGroupBox("Image")
        contentVBox = QVBoxLayout()

        panelWidget = self.CreateImageBox()
        self.CreateCanvasBox()

        contentVBox.addWidget(panelWidget)
        contentBox.setLayout(contentVBox)

        """
        Description box
            contains text description
        """
        descriptionBox = QPlainTextEdit(self.text)

        """
        Panel Id label
        """
        idLabel = QLabel(str(self.panelId))
        vbox.addWidget(contentBox)
        vbox.addWidget(descriptionBox)
        vbox.addWidget(idLabel)

        groupBox.setLayout(vbox)
        groupBox.resize(50, 500)
        return groupBox

    def CreateImageBox(self):
        imgBox = QPixmap("./Models/" + self.img)
        imgLabel = QLabel()
        imgLabel.setPixmap(imgBox)

        return imgLabel

    def CreateCanvasBox(self):
        pass

    def getId(self):
        return self.panelId

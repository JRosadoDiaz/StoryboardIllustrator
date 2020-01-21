from PyQt5.QtWidgets import (QWidget, QLabel, QGroupBox,
                             QPlainTextEdit, QGridLayout)
from PyQt5.QtGui import QPixmap
from Models.PanelCanvas import Canvas


class Panel(QWidget):

    panelId = None
    text = None
    img = 'barn-clipart-vector-25.png'
    imgBoxSize = [800, 500]
    descriptionBoxSize = [800, 200]

    def __init__(self, id, panelText=""):
        print("Panel model has been created")

        self.panelId = id
        self.text = panelText
        super(Panel, self).__init__()

    def buildComponents(self):
        groupBox = QGroupBox("Panel")
        panelGrid = QGridLayout()

        # Content box
        imgWidget = self.CreateImageBox()
        imgWidget.setFixedSize(800, 500)

        # Description box

        descriptionText = QPlainTextEdit(self.text)
        descriptionText.setFixedSize(800, 300)

        # Panel Id

        panelIdLabel = QLabel(str(self.panelId))

        # Add widgets to grid
        panelGrid.addWidget(imgWidget, 0, 0)
        panelGrid.addWidget(descriptionText, 1, 0)
        panelGrid.addWidget(panelIdLabel, 2, 0)

        groupBox.setLayout(panelGrid)

        return groupBox

    def CreateImageBox(self):
        imgBox = QPixmap("./Models/" + self.img)
        imgLabel = QLabel()
        imgLabel.setPixmap(imgBox)
        # imgLabel.setFixedSize(800, 500)

        return imgLabel

    def CreateCanvasBox(self):
        return Canvas()

    def getId(self):
        return self.panelId

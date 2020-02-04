from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QPlainTextEdit, QVBoxLayout, QPushButton)
from Models.PanelModel import Panel
from PyQt5.QtCore import pyqtSignal


class PropertiesMenu(QWidget):

    selectedPanel = None
    deleteSignal = pyqtSignal(int)

    def __init__(self):
        super(PropertiesMenu, self).__init__()
        self.selectedPanel = Panel(1, "Testing Text")
        # self.selectedPanel = panel
        components = []
        layout = QVBoxLayout()

        # Title box
        titleLabel = QLabel("Title")
        components.append(titleLabel)

        self.titleTextBox = QLineEdit()
        components.append(self.titleTextBox)

        # Panel Text
        panelTextLabel = QLabel("Panel Text")
        components.append(panelTextLabel)
        self.panelTextBox = QPlainTextEdit()
        components.append(self.panelTextBox)

        # Upload image button
        uploadButton = QPushButton("Upload Image")
        components.append(uploadButton)

        # Clear image button
        clearButton = QPushButton("Clear Image")
        components.append(clearButton)

        # Delete panel Button
        deleteButton = QPushButton("Delete Panel")
        deleteButton.setStyleSheet('QPushButton {color: red;}')
        deleteButton.clicked.connect(self.deleteButton)
        components.append(deleteButton)

        for x in components:
            layout.addWidget(x)

        # groupBox.setLayout(layout)
        self.setLayout(layout)

    def deleteButton(self):
        # open dialog warning
        print("panel deleted")
        self.deleteSignal.emit(self.selectedPanel)

    def panelChanged(self, panel):
        self.selectedPanel = panel
        self.titleTextBox.text = f"Panel Id {panel.panelId}"
        self.panelTextBox.setPlainText(panel.text)

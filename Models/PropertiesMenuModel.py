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
        layout = QVBoxLayout()

        # Title box
        titleLabel = QLabel("Title")
        layout.addWidget(titleLabel)

        self.titleTextBox = QLineEdit()
        layout.addWidget(self.titleTextBox)

        # Panel Text
        panelTextLabel = QLabel("Panel Text")
        layout.addWidget(panelTextLabel)
        self.panelTextBox = QPlainTextEdit()
        layout.addWidget(self.panelTextBox)

        # Upload image button
        uploadButton = QPushButton("Upload Image")
        layout.addWidget(uploadButton)

        # Clear image button
        clearButton = QPushButton("Clear Image")
        layout.addWidget(clearButton)

        layout.addStretch()
        # Delete panel Button
        deleteButton = QPushButton("Delete Panel")
        deleteButton.setStyleSheet('QPushButton {color: red;}')
        deleteButton.clicked.connect(self.deleteButton)
        layout.addWidget(deleteButton)

        self.setLayout(layout)

    def deleteButton(self):
        # open dialog warning
        print("panel deleted")
        self.deleteSignal.emit(self.selectedPanel)

    def panelChanged(self, panel):
        self.selectedPanel = panel
        self.titleTextBox.text = f"Panel Id {panel.panelId}"
        self.panelTextBox.setPlainText(panel.text)

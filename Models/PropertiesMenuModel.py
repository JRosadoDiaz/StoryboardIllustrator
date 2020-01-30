from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QPlainTextEdit, QVBoxLayout, QPushButton)
from Models.PanelModel import Panel


class PropertiesMenu(QWidget):

    selectedPanel = None

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
        components.append(deleteButton)

        for x in components:
            layout.addWidget(x)

        # groupBox.setLayout(layout)
        self.setLayout(layout)

    def panelChanged(self, panel):
        self.selectedPanel = panel
        self.titleTextBox.text = f"Panel Id {panel.panelId}"
        self.panelTextBox.setPlainText(panel.text)

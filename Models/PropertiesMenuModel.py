from PyQt5.QtWidgets import (QWidget, QDialog, QLabel, QLineEdit,
                             QPlainTextEdit, QVBoxLayout, QPushButton)
from Models.PanelModel import Panel


class PropertiesMenu(QWidget):

    def __init__(self):
        super(PropertiesMenu, self).__init__()
        self.selectedPanel = Panel(1, "Testing Text")
        # self.selectedPanel = panel
        components = []
        layout = QVBoxLayout()

        # Title box
        titleLabel = QLabel("Title")
        components.append(titleLabel)

        titleTextBox = QLineEdit()
        components.append(titleTextBox)

        # Panel Text
        panelTextLabel = QLabel("Panel Text")
        components.append(panelTextLabel)
        panelTextBox = QPlainTextEdit()
        components.append(panelTextBox)

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


class PropertiesMenuDialog(QDialog):

    def __init__(self):
        super(QDialog, self).__init__()
        self.show()

from PyQt5.QtWidgets import QWidget, QPushButton
from PyQt5.QtCore import pyqtSignal


class NewPanelButtonWidget(QWidget):

    clicked = pyqtSignal(int)

    def __init__(self):
        super(NewPanelButtonWidget, self).__init__()

        button = QPushButton("New Panel")
        button.clicked.connect(self.buttonPressed)

    def buttonPressed(self):
        self.clicked.emit(1)

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGroupBox # , QPlainTextEdit


class Panel(QWidget):

    panelId = None
    text = "Testing words"

    def __init__(self, id, panelText):
        print("Hello")
        self.panelId = id
        self.text = panelText
        super(Panel, self).__init__()

    def buildComponents(self):
        groupBox = QGroupBox(f"Panel #{self.panelId}")
        vbox = QVBoxLayout()
        label = QLabel(self.text)
        # decriptionBox = QPlainTextEdit(self.text)
        vbox.addWidget(label)
        # vbox.addWidget(decriptionBox)
        groupBox.setLayout(vbox)

        return groupBox


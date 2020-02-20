from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QAction,
                             qApp)


class StartupWidget(QWidget):

    def __init__(self):
        super(StartupWidget, self).__init__()

        self.buildComponents()

    def buildComponents(self):
        layout = QVBoxLayout()
    
        # Build components
        self.newProject = QPushButton("New Project")
        self.loadProject = QPushButton("Load Project")

        layout.addWidget(self.newProject)
        layout.addWidget(self.loadProject)

        self.setLayout(layout)

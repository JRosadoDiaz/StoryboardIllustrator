from PyQt5.QtWidgets import QMainWindow
from StartupWidget import MainMenu, NewProjectSettingsWidget
from MainWindow import MainWindow


class StartupWindow(QMainWindow):
    windowSize = (1600, 900)

    def __init__(self):
        super(StartupWindow, self).__init__()
        self.resize(self.windowSize[0], self.windowSize[1])
        self.setWindowTitle("Welcome to Storyboard Illustrator")
        self.initUI()

    def initUI(self):
        # Window starts as startup menu
        self.widget = MainMenu()
        self.widget.newProjectButtonClicked.connect(self.changeView)

        self.setCentralWidget(self.widget)

    def changeView(self, signal):
        if signal == 1:
            # New Project was clicked
            self.widget = NewProjectSettingsWidget()
            self.widget.backButtonClicked.connect(self.changeView)
            self.widget.startProjectClicked.connect(self.openMainWindow)
        elif signal == 2:
            self.widget = MainMenu()
            self.widget.newProjectButtonClicked.connect(self.changeView)

        self.setCentralWidget(self.widget)

    def openMainWindow(self, settings):
        print("opening window")
        self.window = MainWindow()
        self.window.setWindowTitle(settings.projectTitle)
        self.window.show()
        self.close()

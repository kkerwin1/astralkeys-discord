from PyQtWidgets import QApplication, QLabel

class GuiManager:
    def __init__(self, main):
        self.main               = main
        self.settingsManager    = self.main.settingsManager
        self.app                = QApplication([])

        

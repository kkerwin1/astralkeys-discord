class SettingsManager:
    def __init__(self, main):
        """
        Class to manage the storage, retention, reproduction, and changing
        of settings.
        """
        
        self.main           = main
        self.fileManager    = self.main.fileManager
        self.settings       = {}

    def getSetting(self, setting):

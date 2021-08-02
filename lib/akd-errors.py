import traceback

class ErrorManager:
    def __init__(self, main):
        """
        Class to manage errors encountered by the program and post them as issues to Github
        for management by the programmer.
        """

        self.main               = main
        self.settingsManager    = self.main.settingsManager
        self.fileManager        = self.main.fileManager
        self.guiManager         = self.main.guiManager
        self.githubManager      = self.main.githubManager
    
    def getSetting(self, setting):
        """
        Obtain a specified setting from SettingsManager.
        """

        return self.settingsManager.getSetting(setting)
    
    def raiseError(self, traceback):
        """
        Provided a traceback, ask the user if they would like to provide
        additional context information, then post to Github in an issue.
        """

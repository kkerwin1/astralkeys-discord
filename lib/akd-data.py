import json

class Parser:
    """
    A parser.
    """

    def __init__(self, manager, _type):
        self.manager    = manager
        self.main       = self.manager.main
        self._type      = _type

class DataManager:
    """
    Class to manage parsers and communicate w/hub and other managers.
    """

    def __init__(self, main):
        self.main               = main
        self.settingsManager    = self.main.settingsManager
        self.settingsParser     = ""
        self.astralParser       = ""
    
    def getSetting(self, setting):
        """
        Ask settingsManager to return value of specified setting.
        """

        self.settingsManager.getSetting(setting)

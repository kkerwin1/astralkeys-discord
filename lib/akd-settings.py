import time, json, io

class JSONManager:
    def __init__(self, manager):
        self.manager    = manager
        self.main       = self.manager.main

    def parseSettings(self, text):
        """
        Parse settings from file.
        """

        decoder = json.JSONDecoder()
        result = decoder.decode(text)
        return result

    def buildJSON(self, dict):
        """
        Given a dictionary, build a JSON string to be written to file.
        """

class SettingsManager:
    def __init__(self, main):
        """
        Class to manage the storage, retention, programmatic reproduction, and
        changing of settings.
        """

        self.main                   = main
        self.fileManager            = self.main.fileManager
        self.settings               = {}
        self.settingsLastUpdated    = 0
        self.jsonManager            = JSONManager(self)

    def parseSettings(self, text):
        """
        Send text to jsonManager for parsing.
        """

        self.jsonManager.parseSettings(text)

    def updateSettings(self):
        """
        Update settings from the file on the hard drive; _open_settings() will
        check to see if there have been any changes. If no changes to the file,
        NameError will be raised as the text variable will be undefined.
        """

        try:
            text = self.fileManager._update_settings()
            self.settingsLastUpdated = int(time.time())
            self.parseSettings(text)
        except NameError:
            pass

    def firstLoad_settings(self):
        """
        Load settings for the first time each time the application is started.
        """

        text = self.fileManager.firstLoad_settings()
        self.settingsLastUpdated = int(time.time())
        self.parseSettings(text)

    def getSetting(self, setting):
        """
        Given a setting name, return its value. Update the settings in RAM from
        the HDD if they are older than 600 seconds.
        """

        if int(time.time()) > self.settingsLastUpdated + 600
            self.updateSettings()
        return self.settings[setting]

    def writeSettings(self):
        """
        Write settings from RAM to files/settings.json.
        """

        text = self.jsonManager.buildJSON(self.settings)
        self.fileManager.save_settings()

import difflib

class FileManager:
    def __init__(self, main):
        self.main               = main
        self.settingsManager    = self.main.settingsManager
        self.settingsText       = ""
        self.oldhash_settings   = 0
        self.uri_astralKeysFile = ""
        self.astralKeysFile     = ""
        self.oldhash_astralkeys = 0

    def getSetting(self, setting):
        """
        Ask settingsManager to return value of specified setting.
        """

        return self.settingsManager.getSetting(setting)

    # ----------
    # AstralKeys
    # ----------

    def getAstralKeysURI(self):
        """
        Get the location (URI) of the Astral Keys data file from the
        settingsManager.
        """

        self.uri_astralKeysFile = self.getSetting("astral_keys_file_uri")

    async def open_astralKeysFile(self):
        """
        Open the data file.
        """

        await _file = open(self.uri_astralKeysFile)
        text = _file.read()
        new_hash = hashFunc(text)
        if new_hash is not self.oldhash_astralkeys:
            self.astralKeysText = text
            self.oldhash_astralkeys = new_hash
        await _file.close()

    def firstLoad_astralKeysFile(self):
        """
        First load of the data file: get the URI, then open the file.
        """

        self.getAstralKeysURI()
        self.open_astralKeysFile()

    # --------
    # Settings
    # --------

    async def firstLoad_settings(self):
        """
        Load the settings file text for the first time.
        """

        await _file = open("file/settings.json")
        text = file.read()
        await file.close()
        self.settingsText = settingsText
        hash = hasFunc(text)
        self.oldHash_settings = hash
        return text

    async def _update_settings(self):
        """
        Update settings from hard disk.
        """

        await _file = open("file/settings.json")
        text = _file.read()
        new_hash = hashFunc(text)
        if new_hash is not self.oldhash_settings:
            self.settingsText = text
            self.oldhash_settings = new_hash
        await _file.close()

    async def save_settings(self):
        """
        Save settings to hard disk.
        """

        await self.settingsManager.generateBuffer()
        await _file = open("file/settings.json")

    async def close_settings(self):
        """
        Close the settings file.
        """

        self.save_settings()
        await self.settingsFile.close()

    async def reload_settings(self):
        """
        Close and re-open the settins file.
        """

        self.close_settings()
        self.open_settings()


    # Start/Stop
    async def start(self):
        """
        Start fileManager.
        """

        self.settingsManager.firstLoad_settings()
        self.firstLoad_astralKeysFile()

    async def stop(self):
        """
        Stop fileManager.
        """
        
        self.close_settings()

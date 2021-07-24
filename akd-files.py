class FileManager:
    def __init__(self, main):
        self.main               = main
        self.settingsManager    = self.main.settingsManager
        self.settingsFile       = ""
        self.uri_astralKeysFile = ""
        self.astralKeysFile     = ""

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
        Get the location (URI) of the Astral Keys data file from the settingsManager.
        """

        self.uri_astralKeysFile = self.getSetting("astral_keys_file_uri")
    
    async def open_astralKeysFile(self):
        """
        Open the data file.
        """

        await self.astralKeysFile = open(self.uri_astralKeysFile)
    
    async def close_astralKeysFile(self):
        """
        Close the data file. We won't write to it.
        """

        await self.astralKeysFile.close()
    
    def reload_astralKeysFile(self):
        """
        Reload the data file.
        """

        self.close_astralKeysFile()
        self.open_astralKeysFile()

    def firstLoad_astralKeysFile(self):
        """
        First load of the data file: get the URI, then open the file.
        """

        self.getAstralKeysURI()
        self.open_astralKeysFile()
    
    # --------
    # Settings
    # --------

    async def open_settings(self):
        await self.settingsFile = open("file/settings.json")

    async def save_settings(self):
        await self.settingsManager.generateBuffer()
        await self.settingsFile.write(self.settingsManager.buffer)
    
    async def close_settings(self):
        self.save_settings()
        await self.settingsFile.close()
    
    async def reload_settings(self):
        self.close_settings()
        self.open_settings()
    

    # Start/Stop
    async def start(self):
        self.open_settings()
        self.firstLoad_astralKeysFile()
    
    async def stop(self):
        self.close_astralKeysFile()
        self.close_settings()

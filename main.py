# requires:
#   python >= 3.5.3
#   discord.py; cf. https://discordpy.readthedocs.io/
#   PyGithub; cf. github.com/PyGithub/PyGithub

from akd-discord import DiscordManager
from akd-gui import GuiManager
from akd-files import FileManager
from akd-settings import SettingsManager
from akd-data import DataManager
from akd-errors import ErrorManager

class Main(self):
    """
    Central management "hub" class that allows other managers to communicate w/one another.
    """

    def __init__(self):
        """
        Structure
        """

        self.errorManager       = ErrorManager(self)
        self.guiManager         = GuiManager(self)
        self.fileManager        = FileManager(self)
        self.dataManager        = DataManager(self)
        self.settingsManager    = SettingsManager(self)
        self.discordManager     = DiscordManager(self)
            
    def start(self):
        """
        Start it
        """

        self.errorManager.start()
        self.guiManager.start()
        self.fileManager.start()
        self.dataManager.start()
        self.settingsManager.start()
        self.discordManager.start()
    
    def stop(self):
        """
        Stop it
        """

        self.discordManager.stop()
        self.settingsManager.stop()
        self.dataManager.stop()
        self.fileManager.stop()
        self.guiManager.stop()
        self.errorManager.stop()

try:
    main = Main()
    main.start()
except:
    main.stop()
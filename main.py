# requires:
#   python >= 3.5.3
#   discord.py; cf. https://discordpy.readthedocs.io/

from akd-discord import DiscordManager
from akd-gui import GuiManager
from akd-files import FileManager
from akd-settings import SettingsManager
from akd-data import DataManager

class Main(self):
    """
    Central management "hub" class that allows other managers to communicate w/one another.
    """

    def __init__(self):
        """
        Structure
        """

        self.guiManager         = GuiManager(self)
        self.fileManager        = FileManager(self)
        self.dataManager        = DataManager(self)
        self.settingsManager    = SettingsManager(self)
        self.discordManager     = DiscordManager(self)
            
    def start(self):
        """
        Start it
        """

        self.guiManager.start()
        self.fileManager.start()
        self.
        self.settingsManager.start()
        self.discordManager.start()
    
    def stop(self):
        """
        Stop it
        """

        self.discordManager.stop()
        self.settingsManager.stop()
        self.fileManager.stop()
        self.guiManager.stop()

try:
    main = Main()
    main.run()
except:
    main.stop()
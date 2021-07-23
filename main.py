# requires:
#   python >= 3.5.3
#   discord.py; cf. https://discordpy.readthedocs.io/

from akd-discord import DiscordManager
from akd-gui import GuiManager
from akd-files import FileManager
from akd-settings import SettingsManager

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
        self.settingsManager    = SettingsManager(self)
        self.discordManager     = DiscordManager(self)
            
    def run(self):
        """
        Start it
        """

        self.guiManager.run()
        self.fileManager.run()
        self.settingsManager.run()
        self.discordManager.run()
    
    def stop(self):
        """
        Stop it
        """

        self.discordManager.stop()
        self.settingsManager.stop()
        self.fileManager.stop()
        self.guiManager.stop()

main = Main()
main.run()
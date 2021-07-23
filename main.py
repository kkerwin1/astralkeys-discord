# requires:
#   python >= 3.5.3
#   discord.py; cf. https://discordpy.readthedocs.io/

from akd-discord import DiscordManager
from akd-gui import GuiManager
from akd-files import FileManager
from akd-settings import SettingsManager

class Main(self):
    def __init__(self):
        self.discordManager = DiscordManager(self)
    
    def run(self):
        self.discordManager.run()

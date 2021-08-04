# requires:
#   python >= 3.5.3
#   discord.py; cf. https://discordpy.readthedocs.io/
#   PyGithub; cf. github.com/PyGithub/PyGithub
#   pyqt

from lib.akd-discord import DiscordManager
from lib.akd-gui import GuiManager
from lib.akd-files import FileManager
from lib.akd-settings import SettingsManager
from lib.akd-data import DataManager
from lib.akd-errors import ErrorManager
from lib.akd-github import GithubManager

import traceback, sys, os

class Main(self):
    """
    Central management "hub" class that allows other managers to communicate
    w/one another.
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

    def raiseError(self, traceback):
        """
        Send a traceback report to ErrorManager, GuiManager, and ultimately
        GitHub for creation of an issue when an error is found.
        """

        self.errorManager.raiseError(traceback)

def main():
    """
    Main function. Start it, stop it, error it, drink tea.
    """

    _main = Main()
    try:
        _main.start()
    except ApplicationClose:
        _main.stop()
    except:
        _main.raiseError(traceback)

if __name__ is __main__:
    """
    This is a script, not a library. It may not be imported into another script.
    Won't work. Sorry!
    """

    main()

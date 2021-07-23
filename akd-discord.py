import discord

tasks = discord.ext.tasks

class DiscordManager(discord.Client):
    """
    Handles discord connection and messaging.
    """

    def __init__(self, main):
        self.main = main        
        self.my_background_task.start()
    
    async def on_ready(self):
        """
        We've logged in.
        """

        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")
    
    @tasks.loop(seconds=self.getSetting("pollingInterval"))
    async def my_background_task(self):
        """
        Run main loop.
        """

        channel = self.get_channel(self.getSetting("channelID"))
        try:
            msg = self.main.obtainUpdate()
            await channel.send(msg)
        except:
            pass
    
    @my_background_task.before_loop
    async def before_my_task(self):
        """
        Tasks to run before each loop execution.
        """

        await self.wait_until_ready()
    
    async def getSetting(self, setting):
        """
        Return live setting from settingsManager for specified setting.
        """
        
        return self.main.settingsManager.settings[setting]

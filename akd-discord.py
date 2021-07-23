import discord

tasks = discord.ext.tasks

class DiscordManager(discord.Client):
    def __init__(self, main):
        self.main = main        
        self.my_background_task.start()
    
    async def on_ready(self):
        print("Logged in as")
        print(self.user.name)
        print(self.user.id)
        print("------")
    
    @tasks.loop(seconds=60)
    async def my_background_task(self):
        channel = self.get_channel(channel_id)
        try:
            msg = self.main.obtainUpdate()
            await channel.send(msg)
        except:
            pass
    
    @my_background_task.before_loop
    async def before_my_task(self):
        await self.wait_until_ready()
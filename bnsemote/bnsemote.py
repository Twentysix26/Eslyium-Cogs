import discord
from discord.ext import commands
import os
from .utils.dataIO import fileIO
from .utils import checks
from glob import glob

class Bns:
    """Bns emotes ¯\_(ツ)_/¯"""

    def __init__(self, bot):
        self.bot = bot
        base_path = 'data/bns/'
        print(base_path)
        files = glob(base_path + '*')
        print(files)
        self.emotes = {}
        for f in files:
            self.emotes[os.path.splitext(f)[0][len(base_path):]] = f
        print(self.emotes)

        
    async def on_message(self, message):
        server = message.server
        channel = message.channel
        author = message.author
        content = message.content
        print('someone typed ' + content)
        for word in content.split():
            if word in self.emotes:   
                print(word + ' was found!')
                await self.bot.send_file(channel, self.emotes[word])
                return # <-- only allow one emote per message

def check_folders():
    if not os.path.exists("data/bns"):
        print("Creating data/bns folder...")
        os.makedirs("data/bns")

def setup(bot):
    n = Bnsemote(bot)
    bot.add_cog(n)

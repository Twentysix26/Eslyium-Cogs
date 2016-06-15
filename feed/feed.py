import discord
from discord.ext import commands
import asyncio
from random import choice as rndchoice
from .utils.dataIO import fileIO
from .utils import checks
import os

defaults = [
    ":cookie:",
    ":sushi:",
    ":fries:",
    ":pizza:",
    ":rice:",
    ":grapes:",
    ":strawberry:",
    ":hamburger:",
    ":cake:",
    ":mushroom:",
    ":dango:",
    ":curry:",
    ":cactus:",
    ":ramen:",
    ":corn:",
    ":sake:",
    ":eggplant:",
    ":banana:",
    ":candy:",
    ":lemon:",
    ":tropical_drink:",
    ":spaghetti:",
    ":custard:",
    ":birthday:",
    ":green_apple:",
    ":melon:",
    ":sweet_potato:",
    ":coffee:",
    ":beer:",
    ":wine_glass:",
    ":fish_cake:",
    ":egg:",
    ":ice_cream:",
    ":lollipop:",
    ":tangerine:",
    ":watermelon:",
    ":bread:",
    ":pineapple:",
    ":rice_cracker:",
    ":shaved_ice:"]

class Feed:
    """Feeding command."""

    def __init__(self, bot):
        self.bot = bot
        self.items = fileIO("data/feed/items.json", "load")

    def save_items(self):
        fileIO("data/slap/items.json", 'save', self.items)

    @commands.command(pass_context=True, invoke_without_command=True)
    async def feed(self, ctx, *, user : discord.Member=None):
        """Force A food Item Down A Users Throat"""
        if ctx.invoked_subcommand is None:
            if user.id == self.bot.user.id:
                user = ctx.message.author
                await self.bot.say(":skull: -Dies- :skull:")
                return
            await self.bot.say("-forces " + (rndchoice(self.items) + " down " +
                               user.name + "'s" + " throat-"))

def check_folders():
    if not os.path.exists("data/feed"):
        print("Creating data/feed folder...")
        os.makedirs("data/feed")

def check_files():
    f = "data/feed/items.json"
    if not fileIO(f, "check"):
        print("Creating empty items.json...")
        fileIO(f, "save", defaults)

def setup(bot):
    check_folders()
    check_files()
    n = Feed(bot)
    bot.add_cog(n)
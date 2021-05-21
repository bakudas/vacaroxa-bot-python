from discord import File
from discord.ext import commands


@commands.command(name="artenilson", help="um mito ao inverso")
async def artenilson(ctx):

    await ctx.send(file=File("./Images/artenilson.png"))


def setup(bot):
    bot.add_command(artenilson)

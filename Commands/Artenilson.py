from discord import File
from discord.ext import commands


@commands.command()
async def artenilson(ctx):

    await ctx.send(file=File("./Images/artenilson.png"))


def setup(bot):
    bot.add_command(artenilson)

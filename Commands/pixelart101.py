from discord.ext import commands
from discord import File


@commands.command(name="pixelart101", help="Aprenda pixelart de uma maneira facilitada")
async def pixelart101(ctx):
    await ctx.send(file=File("./Images/pixelart101.png"))


def setup(bot):
    bot.add_command(pixelart101)

from discord import File
from discord.ext import commands

@commands.command(name='aquaman', help='Aquaman Aquaman Viado')
async def aquaman(ctx):

    await ctx.send(file=File("./Images/Aquaman.png"))


def setup(bot):
    bot.add_command(aquaman)

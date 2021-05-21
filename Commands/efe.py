from discord import File
from discord.ext import commands


@commands.command(name="efe", help="o efe é lindo e podemos provar")
async def efe(ctx):
    await ctx.send(file=File("./Images/effe.jpg"))


def setup(bot):
    bot.add_command(efe)

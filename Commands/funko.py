from discord import File
from discord.ext import commands


@commands.command(name="funko", help="die funko")
async def funko(ctx):

    await ctx.send(file=File("./Images/funko_vaca.png"))


def setup(bot):
    bot.add_command(funko)

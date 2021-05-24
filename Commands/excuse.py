from discord.ext import commands
from discord import File


@commands.command(name="excuse", help="excuse fumito ueda bless")
async def excuse(ctx):
    await ctx.send(file=File("./Images/excuse.gif"))


def setup(bot):
    bot.add_command(excuse)

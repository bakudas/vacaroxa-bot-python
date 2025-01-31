from discord.ext import commands
from discord import File


@commands.command(name="topkek", help="top.. kek!")
async def topkek(ctx):
    await ctx.send(file=File("./Images/topkek.png"))


async def setup(bot):
    bot.add_command(topkek)

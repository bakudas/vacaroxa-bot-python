from discord.ext import commands
from discord import File


@commands.command(name="lul", help="lulululul")
async def lul(ctx):
    await ctx.send(file=File("./Images/lulz.png"))


def setup(bot):
    bot.add_command(lul)

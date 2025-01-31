from discord.ext import commands
from discord import File


@commands.command(name="bangarang", help="melhor video com remix do voice")
async def bangarang(ctx):
    await ctx.send(file=File("./Videos/bangaranggirl.mp4"))


async def setup(bot):
    bot.add_command(bangarang)

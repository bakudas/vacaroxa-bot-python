from discord.ext import commands
from discord import File


@commands.command(name="krai", help="krai bixo")
async def krai(ctx):
    await ctx.send(file=File("./Images/krai.png"))


def setup(bot):
    bot.add_command(krai)

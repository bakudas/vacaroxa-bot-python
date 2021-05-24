from discord.ext import commands
from discord import File


@commands.command(name="fumito", help="Fumito Ueda bless")
async def fumito(ctx):
    await ctx.send(file=File("./Images/fumito.png"))


def setup(bot):
    bot.add_command(fumito)

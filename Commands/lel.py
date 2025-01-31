from discord.ext import commands
from discord import File


@commands.command(name="lel", help="lelelelel")
async def lel(ctx):
    await ctx.send(file=File("./Images/lel.png"))


async def setup(bot):
    bot.add_command(lel)

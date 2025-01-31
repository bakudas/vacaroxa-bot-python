from discord.ext import commands
from discord import File


@commands.command(name="muçei", help="muçei po, buxim chei")
async def muçei(ctx):
    await ctx.send(file=File("./Images/buximchei.png"))


async def setup(bot):
    bot.add_command(muçei)

from discord.ext import commands
from discord import File


@commands.command(name="luiz", help="mood no trabalho do luiz")
async def luiz(ctx):
    await ctx.send(file=File("./Videos/Luiz.mp4"))


async def setup(bot):
    bot.add_command(luiz)

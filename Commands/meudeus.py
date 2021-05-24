from discord.ext import commands
from discord import File


@commands.command(name="meudeus", help="meu deus o que eu tou fazendo aqui..")
async def meudeus(ctx):
    await ctx.send(file=File("./Images/meudeus.png"))


def setup(bot):
    bot.add_command(meudeus)

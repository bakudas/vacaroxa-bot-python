from discord.ext import commands
from discord import File


@commands.command(name="alongamento", help="Imagem com diversos alongamentos")
async def alongamentos(ctx):
    await ctx.send(file=File("./Images/alongamento.png"))


def setup(bot):
    bot.add_command(alongamentos)

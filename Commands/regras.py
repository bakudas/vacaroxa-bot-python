from discord import File
from discord.ext import commands
import random

lista_regras = [
    './Images/regras01.jpg',
    './Images/regras02.png',
    './Images/regras03.jpg',
]


@commands.command(name="regras", help="regras do role")
async def regras(ctx):
    await ctx.send(file=File(random.choice(lista_regras)))


def setup(bot):
    bot.add_command(regras)

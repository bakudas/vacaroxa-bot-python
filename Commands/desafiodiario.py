import twitter
from discord.ext import commands


@commands.command(name="desafiodiario", help="Faz o desafio diário e posta no twitter")
async def desafio_diario(ctx):
    pass


def setup(bot):
    bot.add_command(desafio_diario)

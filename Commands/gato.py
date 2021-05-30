import requests
from discord.ext import commands

site_api = "https://api.thecatapi.com/v1/images/search?mime_types=gif"


@commands.command(name='gato', help="mim dá foto de gatinho")
async def gato(ctx):
    # faz a chamada na api
    get = requests.get(site_api)

    if get.status_code != 200:
        return

    # serializa a resposta
    dict_gatinho = get.json()

    # seta a apenas a url para postar
    url = dict_gatinho[0]['url']

    await ctx.send(url)


def setup(bot):
    bot.add_command(gato)

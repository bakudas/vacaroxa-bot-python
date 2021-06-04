import requests
from discord.ext import commands
from discord import File
import random

site_api = "https://api.thecatapi.com/v1/images/search?mime_types=gif"


@commands.command(name='gato', help="mim dá foto de gatinho")
async def gato(ctx):
    # pick a random number
    rng = random.randint(0, 1000)

    # se o rgn não for 42 entra no fluxo da api de gatinhos
    if rng != 42:
        # faz a chamada na api
        get = requests.get(site_api)

        if get.status_code != 200:
            return

        # serializa a resposta
        dict_gatinho = get.json()

        # seta a apenas a url para postar
        url = dict_gatinho[0]['url']

        await ctx.send(url)
    # se o rgn for 42 envia da fotenha do efe
    else:
        await ctx.send(file=File('./Images/effe.jpg'))


def setup(bot):
    bot.add_command(gato)

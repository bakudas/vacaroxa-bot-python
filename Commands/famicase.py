import random
from discord.ext import commands
from bs4 import BeautifulSoup
import requests
from discord import File

## https://famicase.com/22/softs/001.html
## https://famicase.com/22/softs/001.jpg


fami_source = requests.get("https://famicase.com/22/softs/001.html")

soup = BeautifulSoup(fami_source.content, 'html.parser')

title = soup.h3.string
author = soup.h4.string


@commands.command(name="famicase", help="random famicase cardrigde")
async def famicase(ctx):

    num_rand = random.randrange(000, 253)

    url = "https://famicase.com/22/softs/{:0>3}.html".format(num_rand) if num_rand < 100 \
        else "https://famicase.com/22/softs/{:0}.html".format(num_rand)

    img = "https://famicase.com/22/softs/{:0>3}.jpg".format(num_rand) if num_rand < 100 \
        else "https://famicase.com/22/softs/{:0}.jpg".format(num_rand)

    fami_source = requests.get(url)

    soup = BeautifulSoup(fami_source.content, 'html.parser')

    title = soup.h3.string

    author = soup.h4.string

    msg = '\n' + \
          "Título: " + title + '\n' + \
          "Autor: " + author + '\n' + \
          img

    await ctx.send(msg)


def setup(bot):
    bot.add_command(famicase)

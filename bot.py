# bot.py
from datetime import datetime
import os
import random
import discord
from discord import File
from discord.ext import commands
from dotenv import load_dotenv

# load env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# descrição e intents
description = "Bot do vaca"
intents = discord.Intents.default()
intents.members = True

# inicializando o bot
bot = commands.Bot(command_prefix='$', description=description, intents=intents)


# evento inicial
@bot.event
async def on_ready():
    dt = datetime.now()

    print('-------------------------------------')
    print(f'Logado como: {bot.user.name} às {dt.hour}:{dt.minute}')
    print('-------------------------------------')

    # LOAD COMMANDS
    diretorio = os.curdir + "/Commands"
    for filename in os.listdir(diretorio):
        if filename.endswith(".py"):
            bot.load_extension(f'{diretorio.strip("./")}.{filename.strip(".py")}') #load format Commands.filename


# evento que escuta as mensagens do bot
@bot.event
async def on_message(message):

    # PROCESSO NECESSÁRIO PARA UTILIZAR O EVENTO E OS COMANDOS DE BOT
    await bot.process_commands(message)


# soma
@bot.command(name='soma', help='soma básica do primeiro com o segundo número')
async def soma(ctx, num: int, num2: int):

    await ctx.send(num + num2)


# bakudas videos do youtube
@bot.command(name='bakudas', help='Toca um vídeo da playlist de pixelart do bakudas')
async def bakudas(ctx):

    videos = ["https://www.youtube.com/watch?v=2qYprQwfvYI", "https://www.youtube.com/watch?v=fw7VZiedny8",
              "https://www.youtube.com/watch?v=L1uVrUCcMYc", "https://www.youtube.com/watch?v=7d7Q8S91jmw",
              "https://www.youtube.com/watch?v=seFWi3oO6n8", "https://www.youtube.com/watch?v=DefoA50i15w",
              "https://www.youtube.com/watch?v=duquEtbLC4I", "https://www.youtube.com/watch?v=IPKHPxhTeyA",
              "https://www.youtube.com/watch?v=E9uCHPZ6unw", "https://www.youtube.com/watch?v=nIQMZTnhz_4",
              "https://www.youtube.com/watch?v=IUJTDp7n3nM", "https://www.youtube.com/watch?v=QlOfHx_mF4w",
              "https://www.youtube.com/watch?v=5gR4HKoM-0M", "https://www.youtube.com/watch?v=dVSg2kpnTg0",
              "https://www.youtube.com/watch?v=46zW88Cj0yc", "https://www.youtube.com/watch?v=-wu6ol4WWww",
              "https://www.youtube.com/watch?v=n_ubfPB-Mg4", "https://www.youtube.com/watch?v=t-hLJkhe3v4",
              "https://www.youtube.com/watch?v=hsPuk0I3rKc", "https://www.youtube.com/watch?v=4aZBqJIBq5I",
              "https://www.youtube.com/watch?v=R8zxD9-kFss", "https://www.youtube.com/watch?v=ctov-N9Yq9c",
              "https://www.youtube.com/watch?v=0sAdQwZ8WzQ", "https://www.youtube.com/watch?v=locSdNHBMnU",
              "https://www.youtube.com/watch?v=sBBRACslHns", "https://www.youtube.com/watch?v=Nvxb4-S81cQ",
              "https://www.youtube.com/watch?v=qI2Y1z1wThg", "https://www.youtube.com/watch?v=Gh0ioUPz1pw",
              "https://www.youtube.com/watch?v=4cEf5hYt4cQ", "https://www.youtube.com/watch?v=XLqocGDLpVk",
              "https://www.youtube.com/watch?v=mYaD8r6E3L0", "https://www.youtube.com/watch?v=4XClnvCBnRU",
              "https://www.youtube.com/watch?v=MFpWEk8Aut8", "https://www.youtube.com/watch?v=CW1xIgnECP0",
              "https://www.youtube.com/watch?v=3bsM7HUujfU", "https://www.youtube.com/watch?v=NNVqLOhaJXI",
              "https://www.youtube.com/watch?v=DUPI9hM4UGU", "https://www.youtube.com/watch?v=WnB5kB-FdQw",
              "https://www.youtube.com/watch?v=u5Bu9xRIZ7Q", "https://www.youtube.com/watch?v=o5FoIKQG_0E",
              "https://www.youtube.com/watch?v=_E-AKdmb25E", "https://www.youtube.com/watch?v=tSHb-lsMpCg",
              "https://www.youtube.com/watch?v=bCAeYRROLbw", "https://www.youtube.com/watch?v=c9V8gBSIjyM",
              "https://www.youtube.com/watch?v=076gAckTzms", "https://www.youtube.com/watch?v=iySKJZVoB3k",
              "https://www.youtube.com/watch?v=xN7X1zt4GXA", "https://www.youtube.com/watch?v=673uhY2va6I",
              "https://www.youtube.com/watch?v=a8vZXEV3kKk", "https://www.youtube.com/watch?v=0eRAJ2dK4bw",
              "https://www.youtube.com/watch?v=JDB5SsbEsPw", "https://www.youtube.com/watch?v=XqVku3MTLDo",
              "https://www.youtube.com/watch?v=m13qlkwRk9I", "https://www.youtube.com/watch?v=s3cexCHWoso",
              "https://www.youtube.com/watch?v=tF-ZEUw7zik", "https://www.youtube.com/watch?v=vY-5UnxQXKo",
              "https://www.youtube.com/watch?v=GExZTbtVBRQ", "https://www.youtube.com/watch?v=CU0Ta7gwj9s",
              "https://www.youtube.com/watch?v=zWIMkSrgjpE", "https://www.youtube.com/watch?v=XRShcCzvZ2w",
              "https://www.youtube.com/watch?v=HgYDCxt52wQ", "https://www.youtube.com/watch?v=u6EHVM8CT6A",
              "https://www.youtube.com/watch?v=AZ4oWNHJm2M", "https://www.youtube.com/watch?v=dkgosSDi2_E",
              "https://www.youtube.com/watch?v=QHh_bwyt_VQ", "https://www.youtube.com/watch?v=R_MrWB0_c1U",
              "https://www.youtube.com/watch?v=CJcXcJSAJ44", "https://www.youtube.com/watch?v=Nq7mJM2L7PA",
              "https://www.youtube.com/watch?v=ZxsJwOV2D7Y", "https://www.youtube.com/watch?v=SE8EezHGkVI",
              "https://www.youtube.com/watch?v=qRgZVwzef4Y", "https://www.youtube.com/watch?v=tHErjKVo1iM",
              "https://www.youtube.com/watch?v=Dn1OH5USq8w", "https://www.youtube.com/watch?v=OxXILTmywBI",
              "https://www.youtube.com/watch?v=IQD7MrQTNmI", "https://www.youtube.com/watch?v=RyNFHCu_a3I",
              "https://www.youtube.com/watch?v=3v7b2-Fz0QU", "https://www.youtube.com/watch?v=o3DdKWGhs7A",
              "https://www.youtube.com/watch?v=6anBXexp-AY", "https://www.youtube.com/watch?v=3ADjCeXl2K8",
              "https://www.youtube.com/watch?v=WB8IQ1dlER4", "https://www.youtube.com/watch?v=qukFQVXaUnU",
              "https://www.youtube.com/watch?v=Rj9lbcQbnXE", "https://www.youtube.com/watch?v=3Sf9iMWiiz0",
              "https://www.youtube.com/watch?v=ILmJ-Sm23LA", "https://www.youtube.com/watch?v=0caWvrV5eSM",
              "https://www.youtube.com/watch?v=SmUm7IkZTVE", "https://www.youtube.com/watch?v=tbHWw__1dOo",
              "https://www.youtube.com/watch?v=pRsKNFSTLSc", "https://www.youtube.com/watch?v=JwNqSxOZt-A",
              "https://www.youtube.com/watch?v=M975yK1Qw10", "https://www.youtube.com/watch?v=nQhb7my4LWs",
              "https://www.youtube.com/watch?v=d37ZbDsnCFw", "https://www.youtube.com/watch?v=r3AnaMxP6Es",
              "https://www.youtube.com/watch?v=G9VaVeEu-eg", "https://www.youtube.com/watch?v=UHUc_D9fCNY",
              "https://www.youtube.com/watch?v=1ZjpBAgTpJ4", "https://www.youtube.com/watch?v=xQtkzHCXEeI",
              "https://www.youtube.com/watch?v=J-pmXpVQa1M", "https://www.youtube.com/watch?v=L7kxSXFADU0",
              "https://www.youtube.com/watch?v=ameljJz2SgI", "https://www.youtube.com/watch?v=2jZhFEwKQMw",
              "https://www.youtube.com/watch?v=9F5eF7DLCVI", "https://www.youtube.com/watch?v=3cLaepR8OxQ",
              "https://www.youtube.com/watch?v=2CCfmws1EvI", "https://www.youtube.com/watch?v=1yjaDpKmKXQ",
              "https://www.youtube.com/watch?v=2K-NJS82Z8k", "https://www.youtube.com/watch?v=BAkrOB25Ij0",
              "https://www.youtube.com/watch?v=4z6lvfzbKbI", "https://www.youtube.com/watch?v=vzVcvXmkuHs",
              "https://www.youtube.com/watch?v=R2DoTffhq_c", "https://www.youtube.com/watch?v=QWC5n5Whk-I",
              "https://www.youtube.com/watch?v=WlGzH6vFf-M", "https://www.youtube.com/watch?v=nLeg_PhWryI",
              "https://www.youtube.com/watch?v=yDbHI7Oqvtg", "https://www.youtube.com/watch?v=xTAeBS25nQ4"]
    random_video = random.choice(videos)

    await ctx.send(random_video)


# inicia o bot
bot.run(TOKEN)

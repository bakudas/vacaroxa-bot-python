# bot.py
from datetime import datetime
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import tweepy
import requests

# CARREGA O ENV
load_dotenv()

# TOKEN -> GARANTIR SEGURANÇA DISSO
TOKEN = os.environ.get('DISCORD_TOKEN')

# TWITTER OAUTH
auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))
auth.set_access_token(os.environ.get('TWITTER_TOKEN'), os.environ.get('TOKEN_SECRET'))

# CRIA O OBJETO API DO TWITTER
api = tweepy.API(auth)

# DESCRIÇÃO, HELP E INTENTS
description = "Bot do vaca"
intents = discord.Intents.default()
intents.members = True

# SETANDO O BOT
bot = commands.Bot(command_prefix='$', description=description, intents=intents)


# EVENTO INICIAL
@bot.event
async def on_ready():
    dt = datetime.now()

    print('-------------------------------------')
    print(f'Logado como: {bot.user.name} às {dt.hour}:{dt.minute}')
    print('-------------------------------------')
    print('Comandos carregados: ')

    # CARREGA OS COMANDOS DA PASTA ./Commands
    diretorio = os.curdir + "/Commands"
    for filename in os.listdir(diretorio):
        if filename.endswith(".py"):
            bot.load_extension(
                f'{diretorio.strip("./")}.{filename.strip(".py")}')  # CARREGA NO FORMATO Pasta.nome_arquivo
            print(f'{filename}')


# EVENTO QUE ESCUTA AS MENSAGENS NO SERVIDOR
@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    if message.content.find("#vacadaily") != -1:
        msg = message.content
        anexo = message.attachments

        print(msg)
        print(anexo[0].url)

        with open('desafio.png', 'wb') as imagem:
            resposta = requests.get(anexo[0].url, stream=True)

        await message.channel.send("tou aqui")

    # COROTINA NECESSÁRIA PARA UTILIZAR O EVENTO DE ESCUTA E OS COMANDOS DE BOT
    await bot.process_commands(message)


# INICIA O BOT
bot.run(TOKEN)

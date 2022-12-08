# bot.py
from datetime import datetime, timedelta
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
#import tweepy

# CARREGA O ENV
load_dotenv()

# TOKEN -> GARANTIR SEGURANÇA DISSO
TOKEN = os.environ.get('DISCORD_TOKEN')

# DESCRIÇÃO, HELP E INTENTS
description = "Bot colaborativo do vaca \o/ \n" \
              "Você pode ajudar a melhorá-lo e também adicionar conteúdo. \n" \
              "\n" \
              "repositório do bot: \n" \
              "https://github.com/bakudas/vacaroxa-bot-python"
bot_prefix = "!"
intents = discord.Intents.default()
intents.members = True

# SETANDO O BOT
bot = commands.Bot(command_prefix=bot_prefix, description=description, intents=intents)


# def twitter_api():
#     # TWITTER OAUTH
#     auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))
#     auth.set_access_token(os.environ.get('TWITTER_TOKEN'), os.environ.get('TOKEN_SECRET'))
#
#     # CRIA O OBJETO API DO TWITTER
#     api = tweepy.API(auth)
#
#     return api
#
#
# # CRIANDO A API DO TWITTER
# api = twitter_api()


# EVENTO INICIAL
@bot.event
async def on_ready():
    # CAPTURA A HORA
    formato_hora = "%H:%M"
    hora = datetime.strftime(datetime.now(), formato_hora)

    # REGISTO DE LOGIN DO BOT
    print('-------------------------------------')
    print(f'Logado como: {bot.user.name} às {hora}')
    print('-------------------------------------')
    print('Comandos carregados: ')

    # CARREGA OS COMANDOS DA PASTA ./Commands
    diretorio = os.curdir + "/Commands"
    for filename in os.listdir(diretorio):
        if filename.endswith(".py"):
            # CARREGA NO FORMATO pasta.nome_arquivo
            bot.load_extension(f'{diretorio.strip("./")}.{filename.replace(".py", "")}')
            print(f'{filename}')


# EVENTO QUE ESCUTA AS MENSAGENS NO SERVIDOR
@bot.event
async def on_message(message):
    # CHECA SE FOI O BOT QUE MANDOU A MSG
    if message.author.id == bot.user.id:
        return

    # COROTINA NECESSÁRIA PARA UTILIZAR O EVENTO DE ESCUTA E OS COMANDOS DE BOT
    await bot.process_commands(message)

# INICIA O BOT
bot.run(TOKEN)

# bot.py
from datetime import datetime
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# CARREGA O ENV
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

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

    # CARREGA OS COMANDOS DA PASTA ./Commands
    diretorio = os.curdir + "/Commands"
    for filename in os.listdir(diretorio):
        if filename.endswith(".py"):
            bot.load_extension(f'{diretorio.strip("./")}.{filename.strip(".py")}') # CARREGA NO FORMATO Pasta.nome_arquivo


# EVENTO QUE ESCUTA AS MENSAGENS NO SERVIDOR
@bot.event
async def on_message(message):

    # PROCESSO NECESSÁRIO PARA UTILIZAR O EVENTO E OS COMANDOS DE BOT
    await bot.process_commands(message)


# inicia o bot
bot.run(TOKEN)

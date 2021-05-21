# bot.py
from datetime import datetime
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
import tweepy

# CARREGA O ENV
load_dotenv()

# TOKEN -> GARANTIR SEGURANÇA DISSO
TOKEN = os.environ.get('DISCORD_TOKEN')

# DESCRIÇÃO, HELP E INTENTS
description = "Bot do vaca"
intents = discord.Intents.default()
intents.members = True

# SETANDO O BOT
bot = commands.Bot(command_prefix='$', description=description, intents=intents)


def twitter_api():
    # TWITTER OAUTH
    auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))
    auth.set_access_token(os.environ.get('TWITTER_TOKEN'), os.environ.get('TOKEN_SECRET'))

    # CRIA O OBJETO API DO TWITTER
    api = tweepy.API(auth)

    return api


# CRIANDO A API DO TWITTER
api = twitter_api()


# EVENTO INICIAL
@bot.event
async def on_ready():
    # CAPTURA A HORA
    dt = datetime.now()

    # REGISTO DE LOGIN DO BOT
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
    # CHECA SE FOI O BOT QUE MANDOU A MSG
    if message.author.id == bot.user.id:
        return

    # CHECA A MENSAGEM DO DESAFIO DIARIO
    if message.content.find("#vacadaily") != -1 and 'dungeon keepers' in str(message.author.roles):
        # GUARDA AS INFOS DA MSG
        msg = message.content + "\n" \
                                "\n" \
                                "Utilizem qualquer estilo artístico," \
                                "música, código, 3D, ascii, sinal de fumaça, que seja.. sejam criativos \n" \
                                "\n" \
                                "Todos com as tags #vacaroxa e #vacaDaily serão retuitados \n" \
                                "\n" \
                                "Para feedbacks venham fazer parte da nossa comunidade:\n" \
                                "discord.gg/vacaroxa"

        # GUARDA O ANEXO DA MSG
        anexo = message.attachments

        # MSG SEM ANEXO
        if anexo is None:
            print("mensagem sem anexo!")
            return

        # PERCORRE OS ANEXOS
        for anexos in anexo:
            # SALVA A IMAGEM DE ANEXO
            await anexos.save(f'./desafio/{anexos.filename}')

            # POSTA NO TWITER
            api.update_with_media(f'./desafio/{anexos.filename}', status=msg)

            # LOGA EM CASO DE SUCESSO
            print("foi postado no twitter!")

            # AVISA SE FOI POSTADO NO TWITTER
            await message.channel.send(f"{message.author.display_name}, postei o desafio no twitter (:")

    # COROTINA NECESSÁRIA PARA UTILIZAR O EVENTO DE ESCUTA E OS COMANDOS DE BOT
    await bot.process_commands(message)


# INICIA O BOT
bot.run(TOKEN)

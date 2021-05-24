import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from discord import File
from dotenv import load_dotenv
from discord.ext import commands
import random
from PIL import Image, ImageDraw, ImageFont
import tweepy

# CARREGA O ENV
load_dotenv()

# ESCOPO
scope = ['https://spreadsheets.google.com/feeds']

# CREDENCIAIS DE AUTENTICACAO
credentials = ServiceAccountCredentials.from_json_keyfile_name('gc.json', scope)

# AUTENTICA
gc = gspread.authorize(credentials)

# ABRE A PLANILHA
wks = gc.open_by_key(os.environ.get('GOOGLE_ID_SHEET'))

# SELECIONA A PÁGINA DA PLANILHA
worksheet = wks.get_worksheet(4)  # ABA VOICE DA PLANILHA

# CANAL PARA POSTAR NO TWITTER
canal = ["desafio-diário💡", "bot-trash"]


def twitter_api():
    # TWITTER OAUTH
    auth = tweepy.OAuthHandler(os.environ.get('CONSUMER_KEY'), os.environ.get('CONSUMER_SECRET'))
    auth.set_access_token(os.environ.get('TWITTER_TOKEN'), os.environ.get('TOKEN_SECRET'))

    # CRIA O OBJETO API DO TWITTER
    api = tweepy.API(auth)

    return api


# CRIANDO A API DO TWITTER
api = twitter_api()


@commands.command(name="vacadaily", help="Gera o desadio diário.")
@commands.has_any_role("dungeon keepers")
async def vacadaily(ctx, tema=" "):
    # CHECHA SE O TEMA É RANDOM OU NÃO
    if tema != "random":
        # SE NÃO FOR PEGA O TEXTO DO MENSAGEM, TRATA E SETA A VARIAVEL TEMA
        tema = ctx.message.content.replace('$vacadaily ', '')
    else:
        # LISTA DE TEMAS PARA O COMANDO RANDOM, PUXA DA PLANILHA
        # https://docs.google.com/spreadsheets/d/1NwkKOwXHGchOqBQZYosCos54VC6bsyr-Mg7fMjm79RU/edit#gid=769647817
        planilha_conteudo = worksheet.col_values(1)
        # SETA TEMA COM UMA OPÇÃO RANDOM DA PLANILHA
        tema = random.choice(planilha_conteudo)

    # GARANTIR QUE O TEMA NÃO VENHA EM BRANCO
    if tema == "":
        return

    # SETUP ARQUIVO
    nome_arquivo = f'desafio-{tema.replace(" ", "-")}.png'
    font_titulo = ImageFont.truetype("./Fonts/Gotham-Book.otf", 12)
    font_tema = ImageFont.truetype("./Fonts/Gotham-Bold.otf", 31)

    # ABRE A IMAGEM PARA TRABALHAR
    with Image.open("./desafio/desafio-daily--template.png") as im:
        draw = ImageDraw.Draw(im)

        # ESCREVE O TEMA NA IMAGEM
        draw.text((104, 44), "Tema do dia", (56, 51, 147), font_titulo)
        draw.text((104, 54), f'{tema}', (56, 51, 147), font_tema)

        # SALVA O ARQUIVO
        im.save(f"./desafio/{nome_arquivo}")

        # ENVIA A IMAGEM COM O TEXTO DO TEMA DO DIA
        await ctx.send(tema + " #vacadaily", file=File(f"./desafio/{nome_arquivo}"))

        # GUARDA AS INFOS DA MSG
        msg = tema.upper() + " #vacadaily\n" \
                             "\n" \
                             "Utilizem qualquer estilo artístico," \
                             "música, código, 3D, ascii, sinal de " \
                             "fumaça, que seja.. sejam criativos \n" \
                             "\n" \
                             "Todos com as tags #vacaroxa e " \
                             "#vacaDaily serão retuitados \n" \
                             "\n" \
                             "Para feedbacks venham fazer parte da nossa comunidade:\n" \
                             "discord.gg/vacaroxa"

        if ctx.message.channel.name in canal:
            # POSTA NO TWITER
            api.update_with_media(f"./desafio/{nome_arquivo}", status=msg)

            # AVISA SE FOI POSTADO NO TWITTER
            await ctx.send(f"Olá {ctx.message.author.display_name}, o desafio também foi postado no twitter (:")


def setup(bot):
    bot.add_command(vacadaily)

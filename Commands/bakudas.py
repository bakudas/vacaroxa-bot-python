import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
from discord.ext import commands
import random

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
worksheet = wks.get_worksheet(1)


@commands.command(name="bakudas", help="Um vídeo do youtube do Vaca Roxa")
async def bakudas(ctx):

    # LISTA DE QUOTES PARA O COMANDO
    planilha_links = worksheet.col_values(1)

    await ctx.send(random.choice(planilha_links))

def setup(bot):
    bot.add_command(bakudas)


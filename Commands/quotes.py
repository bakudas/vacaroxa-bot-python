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
credentials = ServiceAccountCredentials.from_json_keyfile_name('credenciais.json', scope)

# AUTENTICA
gc = gspread.authorize(credentials)

# ABRE A PLANILHA
wks = gc.open_by_key('1NwkKOwXHGchOqBQZYosCos54VC6bsyr-Mg7fMjm79RU')

# SELECIONA A PÁGINA DA PLANILHA
worksheet = wks.get_worksheet(0)


@commands.command(name="quote", help="A vaca é muito fofa")
async def quote(ctx):

    # LISTA DE QUOTES PARA O COMANDO
    planilha_quotes = worksheet.col_values(1)

    await ctx.send(random.choice(planilha_quotes))

def setup(bot):
    bot.add_command(quote)
    print("carregou o quote.py")
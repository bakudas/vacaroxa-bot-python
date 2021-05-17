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
worksheet = wks.get_worksheet(2) #ABA VOICE DA PLANILHA


@commands.command(name="especialvoice", help="content aware powered by voice")
@commands.has_any_role("guilda das vacas voadoras", "dungeon master", "curralzinho")
async def especialvoice(ctx, conteudo = " "):

    # LISTA DE QUOTES PARA O COMANDO
    planilha_conteudo = worksheet.col_values(1)

    if conteudo != " ":
        worksheet.update_cell(len(planilha_conteudo) + 1, 1, conteudo)
    else:
        await ctx.send(random.choice(planilha_conteudo))


def setup(bot):
    bot.add_command(especialvoice)



from discord import File
from dotenv import load_dotenv
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont


@commands.command(name="voltaire", help="Gera um quote com a imagem do voltaire.")
async def voltaire(ctx, tema=" "):
    # CHECHA SE O TEMA É RANDOM OU NÃO
    if tema != "random":
        # SE NÃO FOR PEGA O TEXTO DO MENSAGEM, TRATA E SETA A VARIAVEL TEMA
        tema = ctx.message.content.replace('!vacadaily ', '')
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
    nome_arquivo = f'voltaire-{tema.replace(" ", "-")}.png'
    font_titulo = ImageFont.truetype("./Fonts/Gotham-Book.otf", 12)
    font_tema = ImageFont.truetype("./Fonts/Gotham-Bold.otf", 31)

    # ABRE A IMAGEM PARA TRABALHAR
    with Image.open("./imagem/voltaire.jpg") as im:
        draw = ImageDraw.Draw(im)

        # ESCREVE O TEMA NA IMAGEM
        draw.text((104, 44), "Tema do dia", (56, 51, 147), font_titulo)
        draw.text((104, 54), f'{tema}', (56, 51, 147), font_tema)

        # SALVA O ARQUIVO
        im.save(f"./VoltaireQuotes/{nome_arquivo}")

        # ENVIA A IMAGEM COM O TEXTO DO TEMA DO DIA
        await ctx.send(file=File(f"./VoltaireQuotes/{nome_arquivo}"))



async def setup(bot):
    bot.add_command(voltaire)

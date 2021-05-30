from discord.ext import commands
from discord import File
import requests
from PIL import Image, ImageDraw, ImageColor

# const para a altura da imagem gerada
HEIGHT_IMG = 64


@commands.command(name="paleta", help="pega uma paleta de cor aleatória do site lospec")
async def paleta(ctx):
    #pega uma paleta random no site lospec.com
    get_random_path = requests.get("https://lospec.com/palette-list/random")

    # montar a url e captura o json
    json = requests.get(get_random_path.url + '.json')

    # serializa a paleta
    paleta = json.json()

    # faz o tratamento do nome da paleta
    name = paleta['name'].replace(" ", "_")

    # seta a largura da imagem
    width_img = HEIGHT_IMG * len(paleta['colors'])

    # cria uma nova imagem com os tamanhos anteriormente setados
    im = Image.new("RGB", (width_img,HEIGHT_IMG), (128, 128, 128))

    # cria um objeto Draw para desenhar na imagem
    draw = ImageDraw.Draw(im)

    # laço para criar os retangulos coloridos da paleta de cores, percorrendo as cores no dict
    for color in paleta['colors']:
        cor = "#" + color
        draw.rectangle((0, 0, width_img, HEIGHT_IMG), ImageColor.getrgb(cor))
        width_img = width_img - HEIGHT_IMG

    # salva a imagem na pasta Paletas com o nome do arquivo já tratado
    im.save(f"./Paletas/{name}.png", "PNG")

    # envia a mensagem e o arquivo no discord
    await ctx.send(f"Criado por: {paleta['name']}", file=File(f"./Paletas/{name}.png"))


def setup(bot):
    bot.add_command(paleta)

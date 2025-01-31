from discord import File
from discord.ext import commands

@commands.command(name='essabarra', help='Essa barra que é gostar de você..')
async def essabarra(ctx):

    await ctx.send(file=File("./Audios/essabarra.mp3"))


async def setup(bot):
    bot.add_command(essabarra)
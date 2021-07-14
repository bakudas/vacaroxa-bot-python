from discord import File
from discord.ext import commands

@commands.command(name='superhot', help='não tá prestando atenção na porra né.. tão toma ')
async def superhot(ctx):

    await ctx.send(file=File("./Audios/superhot.mp3"))


def setup(bot):
    bot.add_command(superhot)

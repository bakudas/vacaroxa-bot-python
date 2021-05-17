from discord.ext import commands
import random

@commands.command(name="vacalinda", help="A vaca é muito fofa")
async def vacalinda(ctx):

    resposta = [
        'Você que é linde! <:heartpurple:360547787701616640>',
        'https://media.discordapp.net/attachments/337081459577978881/370714930040799233/tenor2.gif'
    ]

    await ctx.send(random.choice(resposta))

def setup(bot):
    bot.add_command(vacalinda)

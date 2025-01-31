import random
from discord.ext import commands

@commands.command(name='d', help='Gira um dado com o número de lados a sua escolha')
async def d(ctx, side: int):

    roll_result = random.randint(1, side)
    name = ctx.author.name

    await ctx.reply(f'{name}, você tirou no dado :game_die:: {roll_result}')

async def setup(bot):
    bot.add_command(d)
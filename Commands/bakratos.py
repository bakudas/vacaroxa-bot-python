from discord import File
from discord.ext import commands


@commands.command(name="bakratos", help="bakudas cosplay de kratos")
async def bakratos(ctx):
    await ctx.send(file=File("./Images/Bakratos.png"))


def setup(bot):
    bot.add_command(bakratos)

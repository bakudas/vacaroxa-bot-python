from discord.ext import commands

@commands.command(name="backup", help="Ver o avatar")
@commands.has_any_role(334695008407912449, 1231289583011102721)
async def backup(ctx):
    await ctx.send(f'Pong! {[message async for message in ctx.bot.history(limit=10)]}')


async def setup(bot):
    bot.add_command(backup)
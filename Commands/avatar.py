from discord import Member
from discord.ext import commands

@commands.command(name="avatar", help="Ver o avatar")
async def avatar(ctx, member:Member = " "):

    if member != " ":
        await ctx.send(member.avatar_url)
    else:
        member = ctx.author
        await ctx.send(member.avatar_url)


async def setup(bot):
    bot.add_command(avatar)
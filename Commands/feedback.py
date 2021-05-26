from discord.ext import commands

link_feedback = "http://j.mp/feedback-como-pedir"
msg = "Vi que tem alguém aqui precisando de feedback e não sabe muito bem como pedir..\n" \
      "Tenho uma leitura para indicar, espero que ajude: \n" \
      f"{link_feedback}"


@commands.command(name="feedback", help="Tá precisando de feedback e não sabe como pedir?")
async def feedback(ctx):
    await ctx.send(msg)


def setup(bot):
    bot.add_command(feedback)

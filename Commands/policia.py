from discord.ext import commands


@commands.command(name="policia", help="fuja da puliça")
async def policia(ctx):
    # PEGA O ID NA FORMA DE MENTION
    user = ctx.message.author.mention

    # MSG PARA O BOT RESPONDER
    msg = "\n" \
          ":rotating_light: :rotating_light: \n" \
          f"{user} declara que para fins de investigação policial, " \
          "não ter envolvimento com este grupo e não saber como " \
          "está no mesmo, provavelmente foi inserido por terceiros, " \
          "declara também que está disposto e apto a colaborar com " \
          "as investigações e se apresentar para depoimento " \
          "caso seja necessário. \n" \
          "<:vacacop:417882011378909184>  <:vacacop:417882011378909184>"

    await ctx.send(msg)


async def setup(bot):
    bot.add_command(policia)

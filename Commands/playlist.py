from discord.ext import commands

# LINK DA PLAYLIST
link = 'https://open.spotify.com/playlist/4x8R48wFEzOlFpWXKK0sNv?si=c5f0795eb9534b22'


@commands.command(name="playlist", help="Playlist Colaborativa Vaca Roxa")
async def playlist(ctx):

    # MENSAGEM DA RESPOSTA
    msg = f"Olá {ctx.message.author.display_name}, está é a nossa playlist colaborativa! \n" \
          f"Fique a vontade para escutar e adicionar suas músicas preferidas também \n" \
          f"\n" \
          f"{link}"
    await ctx.reply(msg)


async def setup(bot):
    bot.add_command(playlist)

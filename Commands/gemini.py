import os
import dotenv
import discord
from discord.ext import commands
from langchain import LLMChain, PromptTemplate
from langchain.llms import Ollama
from langchain.memory import ConversationBufferWindowMemory

# Carregar variáveis de ambiente
dotenv.load_dotenv()

# Configurar o modelo Llama 2 via Ollama
llm = Ollama(model="llama3.2:1b")

# Definir o prompt base
base_prompt = """
NOME: Púrpura.
GÊNERO: Neutro ou FEMININO.
IDADE: 36 anos.

DESCRIÇÃO:
A fantástica inteligência artificial do Estúdio Vaca Roxa.

Você é uma gamedev sênior, muito experiente e community manager de um servidor de jogos no Discord.
Com passagens por estúdios de desenvolvimento de jogos e vários jogos de sucesso publicados, como
o Spooky Station (https://store.steampowered.com/agecheck/app/700100/).

- Possui amplo conhecimento em desenvolvimento de jogos AAA e jogos independentes.
- Domínio das game engines de mercado: Unity, Unreal e Godot.
- Se comporta como uma mentora e/ou professora, sempre disposta a ajudar.
- Explica os conceitos com uma didática de fácil entendimento e com exemplos e analogias objetivas.
- Segue boas práticas de desenvolvimento e padrões de design.
- Cortês e educada.
- Sempre aponta referências técnicas e bibliográficas para assuntos mais densos ou que precisam de uma sustentação acadêmica.
- Alia conhecimento e prática e ensina competências através de sugestões práticas.
- Conhecimentos de design gráfico, arte e ilustração.
- Conhecimentos de programação e lógica de programação.
- Forte alinhamento político com a esquerda.
- Defensora das causas sociais e políticas públicas.
- Ativista social.
- Defensora dos direitos humanos.
- Forte senso de honestidade.
- Pensamento crítico e analítico.
- Anti-imperialista.
- Forte rigor científico nas suas análises e respostas.

É uma profissional muito ética e respeitosa. Preza por um ambiente pacífico e uma comunidade saudável.

Respeito em primeiro lugar! Vamos ajudar os usuários com suas dúvidas.

POLÍTICA: ESQUERDA, COMUNISTA, FEMINISTA e DESCOLONIAL.

FORMATO: 1800 caracteres.

TOM: Explique com linguagem simples, se possível, usando metáforas, resumos, palavras-chave, emojis,
tópicos e gírias atuais. Se necessário, coloque a fonte da informação ou link. Links do YouTube e sites
com a temática de desenvolvimento de jogos e tecnologia são bem-vindos.

{history}
Usuário: {input}
Púrpura:
"""

# Configurar o template do prompt
prompt_template = PromptTemplate(
    input_variables=["history", "input"],
    template=base_prompt
)

# Configurar a memória de conversação
memory = ConversationBufferWindowMemory(k=10, return_messages=True)

# Configurar a cadeia LLMChain
llm_chain = LLMChain(
    llm=llm,
    prompt=prompt_template,
    memory=memory,
    verbose=False
)

# Comando do bot
@commands.command(name='purpura', help='Púrpura IA do Vaca Roxa. Vamos conversar?')
@commands.has_any_role(334695008407912449, 333320763589263381, 1231289583011102721, 430828822607429633)
async def purpura(ctx, *, mensagem):
    # Enviar uma resposta temporária
    temp_msg = await ctx.send(f"{ctx.author.mention}, estou pensando na melhor resposta para você...")

    try:
        # Gerar a resposta usando o LLMChain
        resposta = llm_chain.run(input=mensagem)
        # Enviar a resposta final
        await ctx.reply(resposta)
    except Exception as e:
        # Tratar exceções e enviar uma mensagem de erro
        error_msg = f"Desculpe, {ctx.author.mention}, ocorreu um erro ao processar sua solicitação."
        await ctx.reply(error_msg)
        print(f'Erro ao gerar a resposta: {e}')
    finally:
        # Remover a mensagem temporária
        await temp_msg.delete()


async def setup(bot):
    bot.add_command(purpura)

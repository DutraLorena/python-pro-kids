import os
import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

QUESTIONS = [
    ("Qual animal faz miau?", "gato"),
    ("Quanto é 2 + 3?", "5"),
    ("Qual cor aparece quando misturamos azul e amarelo?", "verde"),
    ("Quanto é 10 - 4?", "6"),
]

scores = {}
active_answers = {}

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.command()
async def ola(ctx):
    await ctx.send('Oi! Eu sou o Bot Kids Quiz. Use !pergunta para jogar.')

@bot.command()
async def pergunta(ctx):
    question, answer = random.choice(QUESTIONS)
    active_answers[ctx.channel.id] = answer.lower()
    await ctx.send(f'Pergunta: {question}')

@bot.command()
async def responder(ctx, *, resposta: str):
    correct = active_answers.get(ctx.channel.id)
    if not correct:
        await ctx.send('Primeiro use !pergunta para receber um desafio.')
        return

    if resposta.lower().strip() == correct:
        user_id = ctx.author.id
        scores[user_id] = scores.get(user_id, 0) + 1
        await ctx.send(f'Parabéns, {ctx.author.mention}! Você acertou e agora tem {scores[user_id]} ponto(s)!')
        del active_answers[ctx.channel.id]
    else:
        await ctx.send('Quase! Tente novamente.')

@bot.command()
async def pontos(ctx):
    points = scores.get(ctx.author.id, 0)
    await ctx.send(f'{ctx.author.mention}, você tem {points} ponto(s).')

if __name__ == '__main__':
    token = os.getenv('DISCORD_BOT_TOKEN')
    if not token:
        raise ValueError('Defina a variável de ambiente DISCORD_BOT_TOKEN antes de iniciar o bot.')
    bot.run(token)

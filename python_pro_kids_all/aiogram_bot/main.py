import asyncio
import os
import random
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
if not TOKEN:
    raise ValueError('Defina a variável de ambiente TELEGRAM_BOT_TOKEN antes de iniciar o bot.')

bot = Bot(token=TOKEN)
dp = Dispatcher()

QUESTIONS = [
    ("Quanto é 4 + 1?", "5"),
    ("Qual fruta é amarela e comprida?", "banana"),
    ("Quanto é 7 - 2?", "5"),
    ("Qual animal late?", "cachorro"),
]

active_questions = {}
scores = {}

@dp.message(Command('start'))
async def start_handler(message: Message):
    await message.answer('Olá! Eu sou o Quiz Kids no Telegram. Use /quiz para começar.')

@dp.message(Command('quiz'))
async def quiz_handler(message: Message):
    question, answer = random.choice(QUESTIONS)
    active_questions[message.chat.id] = answer.lower()
    await message.answer(f'Pergunta: {question}')

@dp.message(Command('pontos'))
async def points_handler(message: Message):
    points = scores.get(message.from_user.id, 0)
    await message.answer(f'Você tem {points} ponto(s).')

@dp.message(F.text)
async def answer_handler(message: Message):
    correct = active_questions.get(message.chat.id)
    if not correct:
        return

    if message.text.lower().strip() == correct:
        user_id = message.from_user.id
        scores[user_id] = scores.get(user_id, 0) + 1
        del active_questions[message.chat.id]
        await message.answer(f'Acertou! Agora você tem {scores[user_id]} ponto(s).')
    else:
        await message.answer('Ainda não foi dessa vez. Tente outra resposta.')

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())

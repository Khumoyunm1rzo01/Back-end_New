

import logging
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator, constantsz

translator = Translator()

API_TOKEN = '5055886499:AAGobKzugq0q9pDXCTN5nF01OJ6mPWc5oH8'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\n I'm translator bot!\n You can use me to translate your projects! \n I'm powered by Python and Django Developer BoyMirzo!")

@dp.message_handler()
async def echo(message: types.Message):
    translation = translator.translate(message.text, dest="")
    await message.answer(translation.text)
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
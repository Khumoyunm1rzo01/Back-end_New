import logging
from aiogram import Bot, bot, Dispatcher, executor, types
from googletrans import Translator, constants

translator = Translator()
translation = translator.translate("Salom bu mening birinchi tarjimon botim! Bu botni mualliflik huquqlarini buzmagan holatda ishlashingiz tarafdoriman!", src="uz", dest="ru", src="uz", dest="en")
API_TOKEN = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

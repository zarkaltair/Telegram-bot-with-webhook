"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '639237490:AAFgastOyZtYYsD9pGg5iNOsVvAOjE5MeFU'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(regexp='(^cat[s]?$|puss)')
async def cats(message: types.Message):
    with open('data/cats.jpg', 'rb') as photo:
        await bot.send_photo(message.chat.id, photo, caption='Cats is here 😺',
                             reply_to_message_id=message.message_id)


@dp.message_handler()
async def echo(message: types.Message):
    await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


# from aiogram import Bot, types
# from aiogram.dispatcher import Dispatcher
# from aiogram.utils import executor


# from config import TOKEN


# bot = Bot(token=TOKEN)
# dp = Dispatcher(bot)

# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
# 	await message.reply('Hello!nWrite me something!')

# @dp.message_handler(commands=['help'])
# async def process_help_command(message: types.Message):
#     await message.reply('Write me something, and I will send this text back to you!')

# @dp.message_handler()
# async def echo_message(msg: types.Message):
# 	await bot.send_message(msg.from_user.id, msg.text)

# if __name__ == '__main__':
# 	executor.start_polling(dp)
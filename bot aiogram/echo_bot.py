import asyncio
import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

from config import TOKEN
from config import PROXY_URL


logging.basicConfig(format=u'%(filename)s [ LINE:%(lineno)+3s ]#%(levelname)+8s [%(asctime)s]  %(message)s', level=logging.INFO)

bot = Bot(token=TOKEN, proxy=PROXY_URL)
dp = Dispatcher(bot)

CAT_BIG_EYES = 'AgADAgAD_KoxG9VJMEqByuFKwZlSkG9lXw8ABCdYNkU_W2ZmWgkBAAEC'
KITTENS = [
    	'AgADAgAD_aoxG9VJMEoIiQjQLgjpcONKXw8ABMOanJERB_J2zw0BAAEC',
    	'AgADAgAD_qoxG9VJMEqTwmaPrmhXKmF6Xw8ABIq2wgu_QkBM-goBAAEC',
    	'AgADAgAD_6oxG9VJMErIQz69tr_T_YJJXw8ABJdloSdtDWQkGg0BAAEC',
]
VOICE = 'AwADAgAD4QIAAtVJMEr4Bi9pw4knCQI'
VIDEO = 'BAADAgAD4gIAAtVJMEqg74p_y4OvdgI'
TEXT_FILE = 'BQADAgAD3wIAAtVJMEqvW4ozbMQXhAI'
VIDEO_NOTE = 'DQADAgAD4AIAAtVJMEp6uTbz3KrD_gI'


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply('Привет!\nИспользуй /help, чтобы узнать список доступных команд!')


@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    msg = text(bold('Я могу ответить на следующие команды:'),
               '/voice', '/photo', '/group', '/note', '/file', '/testpre', '/goodbye', sep='\n')
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['voice'])
async def process_voice_command(message: types.Message):
    await bot.send_voice(message.from_user.id, VOICE, 
    	                 reply_to_message_id=message.message_id)


@dp.message_handler(commands=['photo'])
async def process_photo_command(message: types.Message):
    caption = 'Какие глазки! :eyes:'
    await bot.send_photo(message.from_user.id, CAT_BIG_EYES,
                         caption=emojize(caption),
                         reply_to_message_id=message.message_id)


@dp.message_handler(commands=['group'])
async def process_group_command(message: types.Message):
    media = [InputMediaVideo(VIDEO, 'ёжик и котятки')]
    for photo_id in KITTENS:
        media.append(InputMediaPhoto(photo_id))
    await bot.send_media_group(message.from_user.id, media)


@dp.message_handler(commands=['note'])
async def process_note_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.RECORD_VIDEO_NOTE)
    await asyncio.sleep(1)  # конвертируем видео и отправляем его пользователю
    await bot.send_video_note(message.from_user.id, VIDEO_NOTE)


@dp.message_handler(commands=['file'])
async def process_file_command(message: types.Message):
    user_id = message.from_user.id
    await bot.send_chat_action(user_id, ChatActions.UPLOAD_DOCUMENT)
    await asyncio.sleep(1)  # скачиваем файл и отправляем его пользователю
    await bot.send_document(user_id, TEXT_FILE,
                            caption='Этот файл специально для тебя!')


@dp.message_handler(commands=['testpre'])
async def process_testpre_command(message: types.Message):
    message_text = pre(emojize('''Ха! Не в этот раз :smirk:'''))
    await bot.send_message(message.from_user.id, message_text,
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=['goodbye'])
async def process_testpre_command(message: types.Message):
    message_text = pre(emojize('Давай покеда! :sunglasses:'))
    await bot.send_message(message.from_user.id, message_text,
                           parse_mode=ParseMode.MARKDOWN)


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    message_text = text(emojize('Я не знаю, что с этим делать :astonished:'),
                        italic('\nЯ просто напомню,'), 'что есть',
                        code('команда'), '/help')
    await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)


if __name__ == '__main__':
    executor.start_polling(dp)
import logging
import asyncio
import aiohttp

from aiogram import Bot, types
from aiogram.types import ParseMode
from aiogram.utils.emoji import emojize
from aiogram.dispatcher import Dispatcher
from aiogram.utils.executor import start_polling
from aiogram.utils.markdown import bold, code, italic, text

from config import TOKEN
from config import PROXY_URL


# Configure bot here
API_TOKEN = TOKEN
PROXY = PROXY_URL

# Get my ip URL
GET_IP_URL = 'http://bot.whatismyipaddress.com/'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
loop = asyncio.get_event_loop()
bot = Bot(token=API_TOKEN, loop=loop, proxy=PROXY)
dp = Dispatcher(bot)


async def fetch(url, proxy=None, proxy_auth=None):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, proxy=proxy, proxy_auth=proxy_auth) as response:
            return await response.text()


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    content = []

    # Make request (without proxy)
    ip = await fetch(GET_IP_URL)
    content.append(text(':globe_showing_Americas:', bold('IP:'), code(ip)))
    # This line is formatted to '🌎 *IP:* `YOUR IP`'

    # Make request through proxy
    ip = await fetch(GET_IP_URL, bot.proxy, bot.proxy_auth)
    content.append(text(':locked_with_key:', bold('IP:'), code(ip), italic('via proxy')))
    # This line is formatted to '🔐 *IP:* `YOUR IP` _via proxy_'

    # Send content
    await bot.send_message(message.chat.id, emojize(text(*content, sep='\n')), parse_mode=ParseMode.MARKDOWN)

    # In this example you can see emoji codes: ":globe_showing_Americas:" and ":locked_with_key:"
    # You can find full emoji cheat sheet at https://www.webpagefx.com/tools/emoji-cheat-sheet/
    # For representing emoji codes into real emoji use emoji util (aiogram.utils.emoji)
    # (you have to install emoji module)

    # For example emojize('Moon face :new_moon_face:') is transformed to 'Moon face 🌚'


@dp.message_handler()
async def echo_message(message: types.Message):
    await bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    start_polling(dp, loop=loop, skip_updates=False)
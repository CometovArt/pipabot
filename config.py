from tokens import api_id, api_hash, bot_token, phone_number
from pyrogram import Client
from telegram.ext import Application

# import uvloop
# uvloop.install()

# pymorphy2 используется для склонений при поиске шутеек

import pymorphy2
morph = pymorphy2.MorphAnalyzer()


# Создаем объект логгера

import logging
from datetime import datetime

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO, 
    filename = f'./service/logs/pipa_{datetime.today().strftime("%m-%d")}.log',
    encoding='utf-8'
    )
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


# Создаём объекты сессий
async def post_init(context):
    logger.info('init')
    await userbot.start()
    
async def post_stop(context):
    logger.info('stop')
    await userbot.stop()

# Запускаем бота через BotAPI
application = Application.builder().token(bot_token).post_init(post_init).post_stop(post_stop).build()

# Основной бот
pipabot = Client(
    name='pipabot', 
    api_id=api_id, 
    api_hash=api_hash, 
    bot_token=bot_token, 
    workdir='./service/sessions/'
)

# Юзербот парсинга каналов
userbot = Client(
    name='userbot', 
    api_id=api_id, 
    api_hash=api_hash, 
    phone_number=phone_number, 
    workdir='./service/sessions/'
)


# Задаём пресеты шансов для случайностей

chance = 0.10
big_chance = 0.20
rare_chance = 0.001

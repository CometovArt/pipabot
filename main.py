from telegram import Update
from telegram.ext import filters

from config import userbot, application, logger

# Запускаем все хендлеры
import handlers.brains
import handlers.devs
import handlers.jokes
import handlers.simples
import handlers.specials

import random

from utils.decorator import on_message



@on_message(filters.Regex('привет'))
async def test_app(update, context):
    logger.info(update)
    message = update.message
    await message.reply_text("Hello world!")
    # await context.bot.send_message(chat_id=438257687, text="Hello world!")
    

@userbot.on_message()
async def new_openaiemoji(client, message):
    if random.random() < 0.01: 
        # texts = ['❤️']
        # text = random.choice(texts)
        await userbot.send_reaction(chat_id=message.chat.id, message_id=message.id, emoji='❤️')
    

# Стартуем сессии ботов
def main():
    application.run_polling(allowed_updates=Update.ALL_TYPES)



if __name__ == "__main__":
    main()
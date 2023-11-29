from pyrogram import compose, filters
import asyncio
import random

from config import userbot, pipabot, logger

# Запускаем все хендлеры
import handlers.brains
import handlers.devs
import handlers.jokes
import handlers.simples
import handlers.specials



@userbot.on_message()
async def new_openaiemoji(client, message):
    if random.random() < 0.01: 
        # texts = ['❤️']
        # text = random.choice(texts)
        await userbot.send_reaction(chat_id=message.chat.id, message_id=message.id, emoji='❤️')


# Стартуем сессии ботов
async def main():
    await compose([userbot, pipabot])



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
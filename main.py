from pyrogram import compose
import asyncio

from config import userbot, pipabot

# Запускаем все хендлеры
import handlers.brains
import handlers.devs
import handlers.jokes
import handlers.simples
import handlers.specials



# Стартуем сессии ботов
async def main():
    await compose([userbot, pipabot])



if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
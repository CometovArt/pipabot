# Хэндлер предназначен для ответов отладки, или тех, что находятся в стадии теста

from pyrogram import filters
from config import pipabot, logger

import sqlite3 as sl

    

@pipabot.on_message(filters.command('logger'), group=1)
async def dev_logger(client, message):
    '''Логгируем сообщение.'''
    logger.info(message)
    
    
@pipabot.on_message(filters.command('download'))
async def dev_download(client, message):
    '''Скачиваем медиа.'''
    
    media = None
    
    if message.reply_to_message.photo:
        media = message.reply_to_message.photo.file_id
    elif message.reply_to_message.video:
        media = message.reply_to_message.video.file_id
    elif message.reply_to_message.audio:
        media = message.reply_to_message.audio.file_id
    elif message.reply_to_message.voice:
        media = message.reply_to_message.voice.file_id
    elif message.reply_to_message.animation:
        media = message.reply_to_message.animation.file_id
        
    if media:
        await pipabot.download_media(media)
        
    # Останавливаем отслеживание сообщения другими хендлерами
    message.stop_propagation()
    
    
@pipabot.on_message(filters.command('info'))
async def info(client, message):
    '''Отправляет информацию о боте'''
    
    text = (
        f'**PIPA**\n\n'
        f'Исходный код:\n'
        f'https://github.com/CometovArt/pipabot\n\n'
        f'Контакт автора: @CometovArt\n'
        f'https://boosty.to/cometovart'
    )
    
    await message.reply_text(text)
    

@pipabot.on_message(filters.command('commands'))
async def commands(client, message):
    '''Отправляет информацию о командах'''
    
    text = (
        f'Список доступных команд у PIPA\n\n'
        f'🤡 **Шутки**\n\n'
        f'Если в сообщении будет слово «анекдот» или «паста», то он PIPA пришлёт случайную шутку.\n\n'
        f'Воспользоваться поиском по шуткам можно с помощью текстовых команд:\n'
        f'<pre language=''>анекдот про <запрос>\nпаста про <запрос>\nквн про <запрос></pre>\n\n'
        f'🤖 **Нейросеть**\n\n'
        f'Спросить пипу можно текстовой командой:\n'
        f'<pre language=''>пипа <вопрос> ?</pre>\n'
        f'Если команда отправляется ответом на сообщение пипы, то упоминать пипу не обязательно, '
        f'а сообщение из реплая учтётся в контектсте.'
    )
    
    await message.reply_text(text)
    
    
@pipabot.on_message(filters.command('triggers'))
async def triggers(client, message):
    '''Отправляет информацию о триггерах'''
    
    text = (
        f'Список слов триггеров, на которые реагирует PIPA\n\n'
        f'**Text:**\n'
        f'[🔵] — Да\n'
        f'[🔵] — Нет\n'
        f'[🟢] — Хехе\n'
        f'[🟣] — Утро\n'
        f'[🟢] — Пипа\n'
        f'[🔵] — Пизда\n'
        f'[🟣] — Хуйня\n'
        f'[🟢] — Пук\n'
        f'[🟢] — Халсин\n'
        f'[🟢] — длина моего члена\n'
        f'[🟢] — СМЕРТБ\n'
        f'[🟢] — Мастер\n'
        f'[🟢] — Астарион\n'
        f'\n'
        f'**Stickers:**\n'
        f'[🟣] — Секс\n'
        f'\n'
        f'**GIFs:**\n'
        f'[🟢] — Ква\n'
        f'[🟢] — Спуки\n'
        f'[🟢] — Трахать\n'
        f'[🟢] — Квас\n'
        f'[🟢] — переходи на темную сторону\n'
        f'[🟠] — Думаю\n'
        f'\n'
        f'**Случайные:**\n'
        f'[🟠] — Редкий даун\n'
        f'[🟠] — Кхалиси\n'
        f'[🟠] — dickbot\n'
        f'[🟠] — Грузовик Эмоджи\n'
        f'[🟠] — Упоротый хлеб\n'
    )
    
    await message.reply_text(text)
    
    
@pipabot.on_message(filters.command('dark'))
async def dev_dark_side(client, message):
    '''Заготовка для перевода пипы на тёмную сторону'''
    
    conn = sl.connect('./service/pipa.db')
    cur = conn.cursor()
    
    cur.execute("""SELECT status FROM settings WHERE title = 'dark_side' """)
    result, = cur.fetchone()
    
    if result:
        status = False
    else:
        status = True
    
    cur.execute("""UPDATE settings SET status = ? WHERE title = 'dark_side' """,(status,))
    conn.commit()
    
    conn.close()
    
    # Останавливаем отслеживание сообщения другими хендлерами
    message.stop_propagation()
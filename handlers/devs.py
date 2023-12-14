# Хэндлер предназначен для ответов отладки, или тех, что находятся в стадии теста

from telegram.ext import filters, ApplicationHandlerStop
from config import logger
from utils.decorator import on_message, on_command

import sqlite3 as sl

    

@on_command('logger', group=1)
async def dev_logger(update, context):
    '''Логгируем сообщение.'''
    message = update.message
    logger.info(message)
    
    
@on_command('download')
async def dev_download(update, context):
    '''Скачиваем медиа.'''
    message = update.message
    
    logger.info(update)
    
    media = None
    
    if message.reply_to_message.photo:
        media = message.reply_to_message.photo[3].file_id
    elif message.reply_to_message.video:
        media = message.reply_to_message.video.file_id
    elif message.reply_to_message.audio:
        media = message.reply_to_message.audio.file_id
    elif message.reply_to_message.voice:
        media = message.reply_to_message.voice.file_id
    elif message.reply_to_message.animation:
        media = message.reply_to_message.animation.file_id
        
    if media:
        new_file = await context.bot.get_file(media)
        await new_file.download_to_drive()
        
    # Останавливаем отслеживание сообщения другими хендлерами
    raise ApplicationHandlerStop
    
    
@on_command('info')
async def info(update, context):
    '''Отправляет информацию о боте'''
    message = update.message
    
    text = (
        f'**PIPA**\n\n'
        f'Исходный код:\n'
        f'https://github.com/CometovArt/pipabot\n\n'
        f'Контакт автора: @CometovArt\n'
        f'https://boosty.to/cometovart'
    )
    
    await message.reply_text(text)
    

@on_command('commands')
async def commands(update, context):
    '''Отправляет информацию о командах'''
    message = update.message
    
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
    
    
@on_command('triggers')
async def triggers(update, context):
    '''Отправляет информацию о триггерах'''
    message = update.message
    
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
    
    
@on_command('dark')
async def dev_dark_side(update, context):
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
    raise ApplicationHandlerStop
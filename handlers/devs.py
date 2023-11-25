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
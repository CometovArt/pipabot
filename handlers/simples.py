# Хэндлер предназначен для простых ответов бота на слова-триггеры

from pyrogram import filters
from config import pipabot, chance, big_chance, rare_chance

import random
import asyncio

from utils.spooky import spooky_message



@pipabot.on_message(
    filters=filters.regex('(?:^|(?![а-яёАЯЁ])\W)' + '[дД][аА]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=1)
async def check_da(client, message):
    '''Отвечает «ПИЗДА» на «ДА»'''
    
    if random.random() < chance:
        await message.reply_text(text='ПИЗДА', quote_text=message.matches[0].group(0))


@pipabot.on_message(
    filters=filters.regex('(?:^|(?![а-яёАЯЁ])\W)' + '[нН][еЕ][тТ]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=2)
async def check_net(client, message):
    '''Отвечает «ГОМОСЕКСУАЛЬНЫЙ ОТВЕТ» на «НЕТ»'''
    
    if random.random() < chance:
        await message.reply_text(text='ГОМОСЕКСУАЛЬНЫЙ ОТВЕТ', quote_text=message.matches[0].group(0))
        
        
@pipabot.on_message(
    filters=(
        filters.regex('(?:^|(?![а-яёАЯЁ])\W)' + '[хХhH][аАеЕaAeE][хХhH][аАеЕaAeE]' + '(?=(?![а-яёАЯЁ])\\W|$)') 
        | filters.regex('(?:^|(?![а-яёАЯЁ])\W)' + '[хХhH][аАеЕaAeE] [хХhH][аАеЕaAeE]' + '(?=(?![а-яёАЯЁ])\\W|$)')),
    group=3)
async def check_haha(client, message):
    '''Отвечает «BENIS» на «ХЕХЕ»'''
    
    await message.reply_text(text='BENIS', quote_text=message.matches[0].group(0))
    
    
@pipabot.on_message(
    filters=filters.regex('(?:^|(?![а-яёАЯЁ])\W)' + '[уУ][тТ][рР][оО]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=4)
async def check_utro(client, message):
    '''Отвечает «ХУЮТРО» на «УТРО»'''
    
    if random.random() < big_chance:
        await message.reply_text(text='ХУЮТРО', quote_text=message.matches[0].group(0))
            
    
@pipabot.on_message(
    filters=filters.regex('(?:^|(?![а-яёАЯЁ])\W)' + '[пПpP][иИiI][пПpP][аАыЫуУaA]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=5)
async def check_pipa(client, message):
    '''Отвечает «PIPA» на «ПИПА»'''
    
    await message.reply_text(text='PIPA', quote_text=message.matches[0].group(0))  
        
    
@pipabot.on_message(
    filters=filters.regex('(?:^|(?![а-яёАЯЁ])\W)' + '[пП][иИ][зЗ][дД][аА]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=6)
async def check_pizda(client, message):
    '''Отвечает «ДА» на «ПИЗДА»'''
    
    if random.random() < chance:
        await message.reply_text(text='ДА', quote_text=message.matches[0].group(0))   
            
    
@pipabot.on_message(
    filters=filters.regex('(?:^|(?![а-яёАЯЁ])\W)' + '[хХ][уУ][йЙ][нН][яЯ]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=7)
async def check_huynya(client, message):
    '''Отвечает «САМ ТАКОЙ» на «ХУЙНЯ»'''
    
    if random.random() < big_chance:
        await message.reply_text(text='САМ ТАКОЙ', quote_text=message.matches[0].group(0))   
            
    
@pipabot.on_message(
    filters=filters.regex('(?:^|(?![а-яёАЯЁ])\W)' + '[сС][е,Е][кК][сС]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=8)
async def check_seks(client, message):
    '''Отвечает стикером с Поднебесным на «СЕКС»'''
    
    if random.random() < big_chance:  
        await message.reply_sticker(
            sticker='CAACAgIAAx0CX9oyXQABBzs7ZRV5LVCgtuDLu6dyQiL_yy64xYAAAlYxAALrvNhJA7YZxBeOmCUeBA',
            quote_text=message.matches[0].group(0)
        )
    
    
@pipabot.on_message(
    filters=filters.regex('[кК][вВ][аА][сС]'), 
    group=9)
async def check_kvas(client, message):
    '''Отвечает гифкой с пивом на «КВАС»'''
    
    await message.reply_animation(
        animation='CgACAgQAAx0CX9oyXQABCWmFZWEAAYaXf6qCwYhWGUwLK4n8SxwrAALQAwACsJcUUsyHX0ivKs-pHgQ', 
        quote_text=message.matches[0].group(0)
    )
    
    
@pipabot.on_message(
    filters=filters.regex('(?:^|(?![а-яёАЯЁ])\W)' + '[п,П][уУ][кК]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=10)
async def check_puk(client, message):
    '''Отвечает «ПУК» на «ПУК»'''
    
    if random.random() < chance:  
        await message.reply_text(text='ПУК ПУК')    
    elif random.random() < chance:
        await message.reply_text(text='СРЕНЬК')    
    elif random.random() < rare_chance:
        await message.reply_animation(
            animation='CgACAgIAAx0CX9oyXQABCVrIZV9VMwHWMEvPkswUH7z6Qxm-3kIAAmI2AAIkTAFL0i_g8g3_Fk4eBA',
            quote_text=message.matches[0].group(0)
        )
    else:
        await message.reply_text(text='ПУК')    
    
    
@pipabot.on_message(
    filters=filters.command('start'), 
    group=11)
async def check_start(client, message):
    '''Изящно перекатывается по команде «START»'''
    
    await message.reply_text(text='НА СТАРТ')    
    await asyncio.sleep(3)
    await message.reply_text(text='ВНИМАНИЕ!', quote=False)   
    await asyncio.sleep(3)
    await message.reply_sticker(
        sticker='CAACAgIAAxkBAAMMZR6d6qTQXA54N7Amk3OsyZbRdQYAAqsUAAJWY9FL9pD3iqax64UeBA', 
        quote=False
    )
    
    
@pipabot.on_message(
    filters=filters.regex('[хХ][аА][лЛ][сС][иИ][нН]') | filters.regex('[хХ][аА][лЛ][ьЬ][сС][иИ][нН]'), 
    group=12)
async def check_halsin(client, message):
    '''Отвечает на «ХАЛСИН»'''
    
    texts = ['МОЙ ЛЮБИМЫЙ МИШКА 🧸', 'ХАЛЬСИНЧИК 👉👈', 'ХАЛЬСИН Т-Т-Т-Т-Т-ТРАХАТЬ 🐻🐻🐻']
    text = random.choice(texts)
    await message.reply_text(text=text, quote_text=message.matches[0].group(0))
    
    
@pipabot.on_message(
    filters=filters.regex('[дД][уУ][мМ][аА][лЛтТюЮеЕ]'), 
    group=13)
async def check_dumaem(client, message):
    '''Отвечает гифкой «ДУМАЕМ» на «ДУМАЮ»'''
    
    if random.random() < rare_chance:  
        await message.reply_animation(
            animation='CgACAgIAAxkBAAIGU2Uidj3DNHsCX9nfcSkouc7pEyRaAALdKwACUhPwSaMHg0aOsJqGHgQ', 
            quote_text=message.matches[0].group(0)
        )
        
        
@pipabot.on_message(
    filters=filters.regex('[сС][п,П][уУ][кК][иИ]') | filters.regex('[sS][pP][oO][oO][kK][yY]'), 
    group=14)
async def check_spooky(client, message):
    '''Отвечает гифкой «СПУКИ» на «СПУКИ»'''
    
    await message.reply_animation(
        animation='CgACAgQAAxkBAAIHEGUio6KkdJBP_pmt68QLI9Vv3sZrAALuAgACN5ANUyMp7ayFOkCeHgQ', 
        quote_text=message.matches[0].group(0)
    )
    
    
@pipabot.on_message(
    filters=filters.regex('[тТ][рР][аА][хХ][аА][тТ][ьЬ]') & ~filters.regex('[сС][еЕ][кК][сС]'), 
    group=15)
async def check_trah(client, message):
    '''Отвечает гифкой «ТРАХАТЬ» на «ТРАХАТЬ»'''
    
    await message.reply_animation(
        animation='CgACAgIAAxkBAAIH_WUlCgvTwwRQB0il74UF0wSjAAGhhQACgjQAAoB-KUn0xaf3T4n8dB4E', 
        quote_text=message.matches[0].group(0)
    )
    
    
@pipabot.on_message(
    filters=filters.regex('длина моего члена'), 
    group=16)
async def check_penis_benis(client, message):
    '''Отвечает на «длина моего члена»'''
    
    await message.reply_text(text='Я ТЯ ЁБНУ')
    
    
@pipabot.on_message(
    filters=filters.regex('[пП]ереходи на т[еЕёЁ]мную сторону'), 
    group=17)
async def check_dark_side(client, message):
    '''Переходит на тёмную сторону'''
    
    await message.reply_animation(animation='CgACAgQAAxkBAAIIhWUlazYj4TSmtnsslq0hqblnF6n3AALYAgACOaZMU9mD7HoUBWPoHgQ')
    await message.reply_audio(audio='CQACAgIAAxkBAAIIkGUla6GrlRWZnznz5Zjur-0uhJaRAAKEOQACYvEpSdoMKvqfVWIGHgQ', quote=False)
    

@pipabot.on_message(group=18)
async def check_hit(client, message):
    '''Получает боль'''
    
    if message.sticker and str(message.sticker.file_unique_id) == 'AgADmC0AAvkuqEg':
        await message.reply_text(text='АЙ(')
        

@pipabot.on_message(
    filters=filters.regex('^СМЕРТБ$'), 
    group=19)
async def check_smertb(client, message):
    '''Отвечает на «СМЕРТБ» списком хэллоуиновских фраз'''
    
    text = (spooky_message().upper())
    await message.reply_text(text=text)
    

@pipabot.on_message(
    filters=filters.regex('[мМ][аА][сС][тТ][еЕ][рР]'), 
    group=20)
async def check_master(client, message):
    '''Отвечает на «МАСТЕР»'''
    
    await message.reply_text(text='ДАНЖЕН МАСТЕР', quote_text=message.matches[0].group(0))
    await asyncio.sleep(3)
    await message.reply_text(text='SLAAAAAAVES', quote_text=message.matches[0].group(0))
    
    
@pipabot.on_message(
    filters=filters.regex('[аА][сС][тТ][аА][рР][иИ][оО][нН]'), 
    group=21)
async def check_astarion(client, message):
    '''Отвечает на «АСТАРИОН»'''
    
    await message.reply_text(text='ВОТ БЫ ХУЙ МНЕ ВСТАВИЛ ОН', quote_text=message.matches[0].group(0))
    
    
@pipabot.on_message(
    filters=filters.regex('(?:^|(?![а-яёАЯЁ])\W)' + '[кК][вВ][аА]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=22)
async def check_kva(client, message):
    '''Отвечает гифкой с жабой на «КВА»'''
    
    await message.reply_animation(
        animation='CgACAgQAAx0CX9oyXQABCWm0ZWEDhh79ExGdmolERrrvNLzm_1QAAswCAAIn7A1TNYVJlisMcv0eBA', 
        quote_text=message.matches[0].group(0)
    )
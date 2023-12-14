# Хэндлер предназначен для простых ответов бота на слова-триггеры

from telegram.ext import filters, ApplicationHandlerStop
from config import chance, big_chance, rare_chance, logger
from utils.decorator import on_message, on_command

import random
import asyncio

from utils.spooky import spooky_message



@on_message(
    filters=filters.Regex('(?:^|(?![а-яёАЯЁ])\W)' + '[дД][аА]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=1)
async def check_da(update, context):
    '''Отвечает «ПИЗДА» на «ДА»'''
    message = update.message
    
    if random.random() < chance:
        await message.reply_text(text='ПИЗДА')


@on_message(
    filters=filters.Regex('(?:^|(?![а-яёАЯЁ])\W)' + '[нН][еЕ][тТ]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=2)
async def check_net(update, context):
    '''Отвечает «ГОМОСЕКСУАЛЬНЫЙ ОТВЕТ» на «НЕТ»'''
    message = update.message
    
    if random.random() < chance:
        await message.reply_text(text='ГОМОСЕКСУАЛЬНЫЙ ОТВЕТ')
        
        
@on_message(
    filters=(
        filters.Regex('(?:^|(?![а-яёАЯЁ])\W)' + '[хХhH][аАеЕaAeE][хХhH][аАеЕaAeE]' + '(?=(?![а-яёАЯЁ])\\W|$)') 
        | filters.Regex('(?:^|(?![а-яёАЯЁ])\W)' + '[хХhH][аАеЕaAeE] [хХhH][аАеЕaAeE]' + '(?=(?![а-яёАЯЁ])\\W|$)')),
    group=3)
async def check_haha(update, context):
    '''Отвечает «BENIS» на «ХЕХЕ»'''
    message = update.message
    
    await message.reply_text(text='BENIS')
    
    
@on_message(
    filters=filters.Regex('(?:^|(?![а-яёАЯЁ])\W)' + '[уУ][тТ][рР][оО]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=4)
async def check_utro(update, context):
    '''Отвечает «ХУЮТРО» на «УТРО»'''
    message = update.message
    
    if random.random() < big_chance:
        await message.reply_text(text='ХУЮТРО')
            
    
@on_message(
    filters=filters.Regex('(?:^|(?![а-яёАЯЁ])\W)' + '[пПpP][иИiI][пПpP][аАыЫуУaA]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=5)
async def check_pipa(update, context):
    '''Отвечает «PIPA» на «ПИПА»'''
    message = update.message
    
    await message.reply_text(text='PIPA')  
        
    
@on_message(
    filters=filters.Regex('(?:^|(?![а-яёАЯЁ])\W)' + '[пП][иИ][зЗ][дД][аА]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=6)
async def check_pizda(update, context):
    '''Отвечает «ДА» на «ПИЗДА»'''
    message = update.message
    
    if random.random() < chance:
        await message.reply_text(text='ДА')   
            
    
@on_message(
    filters=filters.Regex('(?:^|(?![а-яёАЯЁ])\W)' + '[хХ][уУ][йЙ][нН][яЯ]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=7)
async def check_huynya(update, context):
    '''Отвечает «САМ ТАКОЙ» на «ХУЙНЯ»'''
    message = update.message
    
    if random.random() < big_chance:
        await message.reply_text(text='САМ ТАКОЙ')   
            
    
@on_message(
    filters=filters.Regex('(?:^|(?![а-яёАЯЁ])\W)' + '[сС][е,Е][кК][сС]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=8)
async def check_seks(update, context):
    '''Отвечает стикером с Поднебесным на «СЕКС»'''
    message = update.message
    
    if random.random() < big_chance:  
        await message.reply_sticker(sticker='CAACAgIAAx0CX9oyXQABBzs7ZRV5LVCgtuDLu6dyQiL_yy64xYAAAlYxAALrvNhJA7YZxBeOmCUeBA')
    
    
@on_message(
    filters=filters.Regex('[кК][вВ][аА][сС]'), 
    group=9)
async def check_kvas(update, context):
    '''Отвечает гифкой с пивом на «КВАС»'''
    message = update.message
    
    await message.reply_animation(animation='CgACAgQAAx0CX9oyXQABCWmFZWEAAYaXf6qCwYhWGUwLK4n8SxwrAALQAwACsJcUUsyHX0ivKs-pHgQ')
    
    
@on_message(
    filters=filters.Regex('(?:^|(?![а-яёАЯЁ])\W)' + '[п,П][уУ][кК]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=10)
async def check_puk(update, context):
    '''Отвечает «ПУК» на «ПУК»'''
    message = update.message
    
    if random.random() < chance:  
        await message.reply_text(text='ПУК ПУК')    
    elif random.random() < chance:
        await message.reply_text(text='СРЕНЬК')    
    elif random.random() < rare_chance:
        await message.reply_animation(animation='CgACAgIAAx0CX9oyXQABCVrIZV9VMwHWMEvPkswUH7z6Qxm-3kIAAmI2AAIkTAFL0i_g8g3_Fk4eBA')
    else:
        await message.reply_text(text='ПУК')    
    
    
@on_command(
    command='start', 
    group=11)
async def check_start(update, context):
    '''Изящно перекатывается по команде «START»'''
    message = update.message
    
    await message.reply_text(text='НА СТАРТ')    
    await asyncio.sleep(3)
    await message.reply_text(text='ВНИМАНИЕ!', quote=False)   
    await asyncio.sleep(3)
    await message.reply_sticker(
        sticker='CAACAgIAAxkBAAMMZR6d6qTQXA54N7Amk3OsyZbRdQYAAqsUAAJWY9FL9pD3iqax64UeBA', 
        quote=False
    )
    
    
@on_message(
    filters=filters.Regex('[хХ][аА][лЛ][сС][иИ][нН]') | filters.Regex('[хХ][аА][лЛ][ьЬ][сС][иИ][нН]'), 
    group=12)
async def check_halsin(update, context):
    '''Отвечает на «ХАЛСИН»'''
    message = update.message
    
    texts = ['МОЙ ЛЮБИМЫЙ МИШКА 🧸', 'ХАЛЬСИНЧИК 👉👈', 'ХАЛЬСИН Т-Т-Т-Т-Т-ТРАХАТЬ 🐻🐻🐻']
    text = random.choice(texts)
    await message.reply_text(text=text)
    
    
@on_message(
    filters=filters.Regex('[дД][уУ][мМ][аА][лЛтТюЮеЕ]'), 
    group=13)
async def check_dumaem(update, context):
    '''Отвечает гифкой «ДУМАЕМ» на «ДУМАЮ»'''
    message = update.message
    
    if random.random() < rare_chance:  
        await message.reply_animation(animation='CgACAgIAAxkBAAIGU2Uidj3DNHsCX9nfcSkouc7pEyRaAALdKwACUhPwSaMHg0aOsJqGHgQ')
        
        
@on_message(
    filters=filters.Regex('[сС][п,П][уУ][кК][иИ]') | filters.Regex('[sS][pP][oO][oO][kK][yY]'), 
    group=14)
async def check_spooky(update, context):
    '''Отвечает гифкой «СПУКИ» на «СПУКИ»'''
    message = update.message
    
    await message.reply_animation(animation='CgACAgQAAxkBAAIHEGUio6KkdJBP_pmt68QLI9Vv3sZrAALuAgACN5ANUyMp7ayFOkCeHgQ')
    
    
@on_message(
    filters=filters.Regex('[тТ][рР][аА][хХ][аА][тТ][ьЬ]') & ~filters.Regex('[сС][еЕ][кК][сС]'), 
    group=15)
async def check_trah(update, context):
    '''Отвечает гифкой «ТРАХАТЬ» на «ТРАХАТЬ»'''
    message = update.message
    
    await message.reply_animation(animation='CgACAgIAAxkBAAIH_WUlCgvTwwRQB0il74UF0wSjAAGhhQACgjQAAoB-KUn0xaf3T4n8dB4E')
    
    
@on_message(
    filters=filters.Regex('длина моего члена'), 
    group=16)
async def check_penis_benis(update, context):
    '''Отвечает на «длина моего члена»'''
    message = update.message
    
    await message.reply_text(text='Я ТЯ ЁБНУ')
    
    
@on_message(
    filters=filters.Regex('[пП]ереходи на т[еЕёЁ]мную сторону'), 
    group=17)
async def check_dark_side(update, context):
    '''Переходит на тёмную сторону'''
    message = update.message
    
    await message.reply_animation(animation='CgACAgQAAxkBAAIIhWUlazYj4TSmtnsslq0hqblnF6n3AALYAgACOaZMU9mD7HoUBWPoHgQ')
    await message.reply_audio(audio='CQACAgIAAxkBAAIIkGUla6GrlRWZnznz5Zjur-0uhJaRAAKEOQACYvEpSdoMKvqfVWIGHgQ', quote=False)
    

@on_message(filters.Sticker.ALL, group=18)
async def check_hit(update, context):
    '''Получает боль'''
    message = update.message
    logger.info(message.sticker)
    
    if message.sticker and str(message.sticker.file_unique_id) == 'AgADmC0AAvkuqEg':
        await message.reply_text(text='АЙ(')
        

@on_message(
    filters=filters.Regex('^СМЕРТБ$'), 
    group=19)
async def check_smertb(update, context):
    '''Отвечает на «СМЕРТБ» списком хэллоуиновских фраз'''
    message = update.message
    
    text = (spooky_message().upper())
    await message.reply_text(text=text)
    

@on_message(
    filters=filters.Regex('[мМ][аА][сС][тТ][еЕ][рР]'), 
    group=20)
async def check_master(update, context):
    '''Отвечает на «МАСТЕР»'''
    message = update.message
    
    await message.reply_text(text='ДАНЖЕН МАСТЕР')
    await asyncio.sleep(3)
    await message.reply_text(text='SLAAAAAAVES')
    
    
@on_message(
    filters=filters.Regex('[аА][сС][тТ][аА][рР][иИ][оО][нН]'), 
    group=21)
async def check_astarion(update, context):
    '''Отвечает на «АСТАРИОН»'''
    message = update.message
    
    await message.reply_text(text='ВОТ БЫ ХУЙ МНЕ ВСТАВИЛ ОН')
    
    
@on_message(
    filters=filters.Regex('(?:^|(?![а-яёАЯЁ])\W)' + '[кК][вВ][аА]' + '(?=(?![а-яёАЯЁ])\\W|$)'), 
    group=22)
async def check_kva(update, context):
    '''Отвечает гифкой с жабой на «КВА»'''
    message = update.message
    
    await message.reply_animation(animation='CgACAgQAAx0CX9oyXQABCWm0ZWEDhh79ExGdmolERrrvNLzm_1QAAswCAAIn7A1TNYVJlisMcv0eBA')
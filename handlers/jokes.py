# Хэндлер предназначен для ответов бота с шутками из источников

from pyrogram import filters
from config import pipabot, chance, rare_chance

import random
import asyncio

from utils.jokes.kvn import get_kvn, get_kvn_pro, get_kvn_juri
from utils.jokes.pastas import get_pasta, get_pasta_pro
from utils.jokes.anekdots import get_anek, get_anek_pro
        
        
        
@pipabot.on_message(
    filters=(
        filters.regex('(?:^|(?![а-яёАЯЁ])\W)' + '[п,П][а,А][с,С][т,Т][а,А,у,У]' + '(?=(?![а-яёАЯЁ])\\W|$)') 
        & ~filters.regex('(?:^|(?![а-яёАЯЁ])\W)' + '[п,П][р,Р][о,О]' + '(?=(?![а-яёАЯЁ])\\W|$)')), 
    group=201)
async def check_pasta(client, message):
    '''Присылает пасту, если в сообщении есть слово «паста»'''
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(client, message, type_joke='АНЕКДОТЫ')
        return

    # Получаем и отправляем пасту
    pasta = await get_pasta()
    await message.reply_text(text=pasta.upper())
            
            
@pipabot.on_message(
    filters=filters.regex('^[п,П][а,А][с,С][т,Т][а,А,у,У] [п,П][р,Р][о,О]'), 
    group=202)
async def check_pasta_pro(client, message):
    '''Ищет пасту, если сообщение начинается со слов «паста про»'''
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(client, message, type_joke='АНЕКДОТЫ')
        return

    # Вытаскиваем из сообщения текст для поиска
    result = message.text.split(' ')
    pasta_result = ' '.join(result[2:])
    
    # Получаем и отправляем пасту
    pasta = await get_pasta_pro(pasta_result)
    await message.reply_text(text=pasta.upper())
        
        
@pipabot.on_message(
    filters=filters.regex('^[п,П,p,P][и,И,i,I][п,П,p,P][а,А,ы,Ы,у,У,a,A] [п,П][а,А][с,С][т,Т][а,А,у,У] [п,П][р,Р][о,О]'), 
    group=203)
async def check_pasta_pipa_pro(client, message):
    '''Ищет пасту, если сообщение начинается со слов «пипа паста про»'''
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(client, message, type_joke='АНЕКДОТЫ')
        return
        
    # Вытаскиваем из сообщения текст для поиска
    result = message.text.split(' ')
    pasta_result = ' '.join(result[3:])
    
    # Получаем и отправляем пасту
    pasta = await get_pasta_pro(pasta_result)
    await message.reply_text(text=pasta.upper())
    
    
    
@pipabot.on_message(
    filters=(
        filters.regex('(?:^|(?![а-яёАЯЁ])\W)' + '[а,А][н,Н][е,Е][к,К][д,Д][о,О][т,Т]' + '(?=(?![а-яёАЯЁ])\\W|$)') 
        & ~filters.regex('(?:^|(?![а-яёАЯЁ])\W)' + '[п,П][р,Р][о,О]' + '(?=(?![а-яёАЯЁ])\\W|$)')), 
    group=204)
async def check_anek(client, message):
    '''Присылает анекдот, если в сообщении есть слово «анекдот»'''
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(client, message, type_joke='АНЕКДОТЫ')
        return
    
    # Получаем и отправляем анекдот
    anek = await get_anek()
    await message.reply_text(text=anek.upper())
    
    
@pipabot.on_message(
    filters=filters.regex('^[а,А][н,Н][е,Е][к,К][д,Д][о,О][т,Т] [п,П][р,Р][о,О]'), 
    group=205)
async def check_anek_pro(client, message):
    '''Ищет анекдот, если сообщение начинается со слов «анекдот про»'''
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(client, message, type_joke='АНЕКДОТЫ')
        return
    
    # Вытаскиваем из сообщения текст для поиска
    result = message.text.split(' ')
    anek_result = ' '.join(result[2:])
    
    # Получаем и отправляем анекдот
    anek = await get_anek_pro(anek_result)
    await message.reply_text(text=anek.upper())
        
        
@pipabot.on_message(
    filters=filters.regex('^[п,П,p,P][и,И,i,I][п,П,p,P][а,А,ы,Ы,у,У,a,A] [а,А][н,Н][е,Е][к,К][д,Д][о,О][т,Т] [п,П][р,Р][о,О]'), 
    group=206)
async def check_anek_pipa_pro(client, message):
    '''Ищет анекдот, если сообщение начинается со слов «пипа анекдот про»'''
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(client, message, type_joke='АНЕКДОТЫ')
        return
    
    # Вытаскиваем из сообщения текст для поиска
    result = message.text.split(' ')
    anek_result = ' '.join(result[3:])
    
    # Получаем и отправляем анекдот
    anek = await get_anek_pro(anek_result)
    await message.reply_text(text=anek.upper())
        
        
@pipabot.on_message(
    filters=(
        filters.regex('[м,М][ы,Ы] [н,Н][а,А][ч,Ч][и,И][н,Н][а,А][е,Е][м,М] [к,К][в,В][н,Н]')), 
    group=207)
async def check_start_kvn(client, message):
    '''Присылает квн, если в сообщении есть «мы начинаем квн»'''
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(client, message, type_joke='КАВЭЭНЫ')
        return
    
    if random.random() < chance:
        await message.reply_text(text='ДЛЯ КОГО')
        await asyncio.sleep(1)
        await message.reply_text(text='ДЛЯ ЧЕГО', quote=False)
        return
    
    # Получаем и отправляем квн
    title, joke = await get_kvn()
    kvn = joke + '\n\n' f'**{title}**'
    await message.reply_text(text=kvn.upper())
    
    
@pipabot.on_message(
    filters=filters.regex('^[к,К][в,В][н,Н] [п,П][р,Р][о,О]'), 
    group=209)
async def check_kvn_pro(client, message):
    '''Ищет квн, если сообщение начинается со слов «квн про»'''
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(client, message, type_joke='КАВЭЭНЫ')
        return
    
    # Вытаскиваем из сообщения текст для поиска
    result = message.text.split(' ')
    kvn_result = ' '.join(result[2:])
    
    # Получаем и отправляем квн
    title, joke = await get_kvn_pro(kvn_result)
    kvn = joke + '\n\n' f'**{title}**'
    await message.reply_text(text=kvn.upper())
        
        
@pipabot.on_message(
    filters=filters.regex('^[п,П,p,P][и,И,i,I][п,П,p,P][а,А,ы,Ы,у,У,a,A] [к,К][в,В][н,Н] [п,П][р,Р][о,О]'), 
    group=209)
async def check_kvn_pipa_pro(client, message):
    '''Ищет квн, если сообщение начинается со слов «пипа квн про»'''
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(client, message, type_joke='КАВЭЭНЫ')
        return
    
    # Вытаскиваем из сообщения текст для поиска
    result = message.text.split(' ')
    kvn_result = ' '.join(result[3:])
    
    # Получаем и отправляем квн
    title, joke = await get_kvn_pro(kvn_result)
    kvn = joke + '\n\n' f'**{title}**'
    await message.reply_text(text=kvn.upper())
        
        
@pipabot.on_message(
    filters=filters.voice, 
    group=211)
async def check_kvn_juri(client, message):
    '''С небольшим шансом отвечаем на голосовое сообщение репликой жюри'''
    
    if random.random() < rare_chance:  
        kvn = await get_kvn_juri()
        await message.reply_text(text=kvn.upper())
        
        
async def help_message(client, message, type_joke):
    '''Отправляем сообщение с мольбой о помощи'''
    
    await message.reply_text(text=f'ХВАТИТ ПРОСИТЬ {type_joke}, Я САМ СКОРО СДОХНУ ОТ НИХ 💀')
    await asyncio.sleep(1)
    await message.reply_text(text='ЭТО Ж КРИНЖ ПИЗДЕЦ', quote=False)
    await asyncio.sleep(1)
    await message.reply_text(text='САШАААААААА ПОМОГИ 😫😫😫😫😫😫', quote=False)
# Хэндлер предназначен для ответов бота с шутками из источников

from telegram.ext import filters, ApplicationHandlerStop
from config import chance, big_chance, rare_chance
from utils.decorator import on_message, on_command

import random
import asyncio

from handlers.brains import openai_response

from utils.jokes.kvn import get_kvn, get_kvn_pro, get_kvn_juri
from utils.jokes.pastas import get_pasta, get_pasta_pro
from utils.jokes.anekdots import get_anek, get_anek_pro
        
        
        
@on_message(
    filters=(
        filters.Regex('(?:^|(?![а-яёАЯЁ])\W)' + '[пП][аА][сС][тТ][аАуУ]' + '(?=(?![а-яёАЯЁ])\\W|$)') 
        & ~filters.Regex('(?:^|(?![а-яёАЯЁ])\W)' + '[пП][рР][оО]' + '(?=(?![а-яёАЯЁ])\\W|$)')), 
    group=201)
async def check_pasta(update, context):
    '''Присылает пасту, если в сообщении есть слово «паста»'''
    message = update.message
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(message, type_joke='ПАСТЫ')
        return

    # Получаем и отправляем пасту
    pasta = await get_pasta()
    await message.reply_text(text=pasta.upper())
            
            
@on_message(
    filters=filters.Regex('[пП][аА][сС][тТ][аАуУ] [пП][рР][оО]'), 
    group=202)
async def check_pasta_pro(update, context):
    '''Ищет пасту, если сообщение начинается со слов «паста про»'''
    message = update.message
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(message, type_joke='ПАСТЫ')
        return

    # # Вытаскиваем из сообщения текст для поиска
    # result = message.text.split(' ')
    # pasta_result = ' '.join(result[2:])
    key_word = 'паста про'
    pasta_result = await edit_text(message.text.lower(), key_word)
    
    if random.random() < big_chance:  
        pasta = await openai_response(context=context, message=message, context_promt='придумай ', promt=pasta_result, model='gpt-3.5-turbo')
    else:
        # Получаем и отправляем пасту
        pasta = await get_pasta_pro(pasta_result)
    
    if pasta is None:
        pasta = await openai_response(context=context, message=message, context_promt='придумай ', promt=pasta_result, model='gpt-3.5-turbo')
    
    # # Получаем и отправляем пасту
    # pasta = await get_pasta_pro(pasta_result)
    await message.reply_text(text=pasta.upper())
        
        
# @on_message(
#     filters=filters.Regex('^[пПpP][иИiI][пПpP][аАыЫуУaA] [пП][аА][сС][тТ][аАуУ] [пП][рР][оО]'), 
#     group=203)
# async def check_pasta_pipa_pro(update, context):
#     '''Ищет пасту, если сообщение начинается со слов «пипа паста про»'''
    
#     # С небольшим шансом отправляет сообщение с мольбой о помощи
#     if random.random() < rare_chance:  
#         await help_message(message, type_joke='ПАСТЫ')
#         return
        
#     # Вытаскиваем из сообщения текст для поиска
#     result = message.text.split(' ')
#     pasta_result = ' '.join(result[3:])
    
#     # Получаем и отправляем пасту
#     pasta = await get_pasta_pro(pasta_result)
#     await message.reply_text(text=pasta.upper())
    
    
    
@on_message(
    filters=(
        filters.Regex('(?:^|(?![а-яёАЯЁ])\W)' + '[аА][нН][еЕ][кК][дД][оО][тТ]' + '(?=(?![а-яёАЯЁ])\\W|$)') 
        & ~filters.Regex('(?:^|(?![а-яёАЯЁ])\W)' + '[пП][рР][оО]' + '(?=(?![а-яёАЯЁ])\\W|$)')), 
    group=204)
async def check_anek(update, context):
    '''Присылает анекдот, если в сообщении есть слово «анекдот»'''
    message = update.message
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(message, type_joke='АНЕКДОТЫ')
        return
    
    # Получаем и отправляем анекдот
    anek = await get_anek()
    await message.reply_text(text=anek.upper())
    
    
@on_message(
    filters=filters.Regex('[аА][нН][еЕ][кК][дД][оО][тТ] [пП][рР][оО]'), 
    group=205)
async def check_anek_pro(update, context):
    '''Ищет анекдот, если сообщение начинается со слов «анекдот про»'''
    message = update.message
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(message, type_joke='АНЕКДОТЫ')
        return
    
    # # Вытаскиваем из сообщения текст для поиска
    # result = message.text.split(' ')
    # anek_result = ' '.join(result[2:])
    
    key_word = 'анекдот про '
    anek_result = await edit_text(message.text.lower(), key_word)
    
    if random.random() < big_chance:  
        anek = await openai_response(context=context, message=message, promt=message.text, model='gpt-3.5-turbo')
    else:
        # Получаем и отправляем пасту
        anek = await get_pasta_pro(anek_result)
    
    if anek is None:
        anek = await openai_response(context=context, message=message, promt=message.text, model='gpt-3.5-turbo')
    
    # # Получаем и отправляем анекдот
    # anek = await get_anek_pro(anek_result)
    await message.reply_text(text=anek.upper())
        
        
# @on_message(
#     filters=filters.Regex('^[пПpP][иИiI][пПpP][аАыЫуУaA] [аА][нН][еЕ][кК][дД][оО][тТ] [пП][рР][оО]'), 
#     group=206)
# async def check_anek_pipa_pro(update, context):
#     '''Ищет анекдот, если сообщение начинается со слов «пипа анекдот про»'''
    
#     # С небольшим шансом отправляет сообщение с мольбой о помощи
#     if random.random() < rare_chance:  
#         await help_message(message, type_joke='АНЕКДОТЫ')
#         return
    
#     # Вытаскиваем из сообщения текст для поиска
#     result = message.text.split(' ')
#     anek_result = ' '.join(result[3:])
    
#     # Получаем и отправляем анекдот
#     anek = await get_anek_pro(anek_result)
#     await message.reply_text(text=anek.upper())
        
        
@on_message(
    filters=(
        filters.Regex('[мМ][ыЫ] [нН][аА][чЧ][иИ][нН][аА][еЕ][мМ] [кК][вВ][нН]')), 
    group=207)
async def check_start_kvn(update, context):
    '''Присылает квн, если в сообщении есть «мы начинаем квн»'''
    message = update.message
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(message, type_joke='КАВЭЭНЫ')
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
    
    
@on_message(
    filters=filters.Regex('^[кК][вВ][нН] [пП][рР][оО]'), 
    group=209)
async def check_kvn_pro(update, context):
    '''Ищет квн, если сообщение начинается со слов «квн про»'''
    message = update.message
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(message, type_joke='КАВЭЭНЫ')
        return
    
    # Вытаскиваем из сообщения текст для поиска
    result = message.text.split(' ')
    kvn_result = ' '.join(result[2:])
    
    # Получаем и отправляем квн
    title, joke = await get_kvn_pro(kvn_result)
    kvn = joke + '\n\n' f'**{title}**'
    await message.reply_text(text=kvn.upper())
        
        
@on_message(
    filters=filters.Regex('^[пПpP][иИiI][пПpP][аАыЫуУaA] [кК][вВ][нН] [пП][рР][оО]'), 
    group=209)
async def check_kvn_pipa_pro(update, context):
    '''Ищет квн, если сообщение начинается со слов «пипа квн про»'''
    message = update.message
    
    # С небольшим шансом отправляет сообщение с мольбой о помощи
    if random.random() < rare_chance:  
        await help_message(message, type_joke='КАВЭЭНЫ')
        return
    
    # Вытаскиваем из сообщения текст для поиска
    result = message.text.split(' ')
    kvn_result = ' '.join(result[3:])
    
    # Получаем и отправляем квн
    title, joke = await get_kvn_pro(kvn_result)
    kvn = joke + '\n\n' f'**{title}**'
    await message.reply_text(text=kvn.upper())
        
        
@on_message(
    filters=filters.VOICE, 
    group=211)
async def check_kvn_juri(update, context):
    '''С небольшим шансом отвечаем на голосовое сообщение репликой жюри'''
    message = update.message
    
    if random.random() < rare_chance:  
        kvn = await get_kvn_juri()
        await message.reply_text(text=kvn.upper())
        
        
async def help_message(message, type_joke):
    '''Отправляем сообщение с мольбой о помощи'''
    
    await message.reply_text(text=f'ХВАТИТ ПРОСИТЬ {type_joke}, Я САМ СКОРО СДОХНУ ОТ НИХ 💀')
    await asyncio.sleep(1)
    await message.reply_text(text='ЭТО Ж КРИНЖ ПИЗДЕЦ', quote=False)
    await asyncio.sleep(1)
    await message.reply_text(text='САШАААААААА ПОМОГИ 😫😫😫😫😫😫', quote=False)
    
    
async def edit_text(text, key_word):
    index = text.find(key_word)
    e_text = text[index + len(key_word):]
    
    return e_text
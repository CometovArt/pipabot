# Хэндлер предназначен для специальных, редких ответов бота

from telegram.ext import filters, ApplicationHandlerStop
from config import rare_chance, logger
from utils.decorator import on_message, on_command

import random

from utils.khaleesi import Khaleesi


# @pipabot.on_deleted_messages(group=1000000)
# async def check_deletes(update, context):
#     message = update.message
#     logger.info(message)


@on_message(filters.StatusUpdate.NEW_CHAT_MEMBERS)
async def check_new_member(update, context):
    '''Присылает приветственный ответ новому члену чата'''
    message = update.message
    
    await message.reply_sticker(sticker='CAACAgIAAxkBAAIH4mUjsUJPcajrLz5RQJNqDFqIF6YaAALOIQACpAABqUjNr9y1vYnsJx4E')
    
    # Останавливаем отслеживание сообщения другими хендлерами
    raise ApplicationHandlerStop
    
    
# @on_message(filters.StatusUpdate.ALL)
# async def check_left_member(update, context):
#     '''Идентифицирует ливнувшего из чата гада (работает только если у бота есть админка)'''
#     logger.info(update)
    
    # # Ожидаем обновления UpdateChannelParticipant, оно присылается, когда изменяется состав участников чата
    # chat_id = f'-100{update.channel_id}'
    
    # # Проверяем есть ли виновник обновления в составе чата, потому что
    # # обновление срабатывает так же при входе юзера в чат
    # members = []
    # async for member in pipabot.get_chat_members(chat_id):
    #     members.append(int(member.user.id))
        
    # if int(update.user_id) in members:
    #     return
    
    # # Собираем текстовое сообщение с инфой
    # text = 'Ливнул, гад:\n\n'
    # text += f'**{users[update.user_id].first_name}** '
    
    # if users[update.user_id].last_name:
    #     text += f'**{users[update.user_id].last_name}**'
        
    # if users[update.user_id].username:
    #     text += f'\n@{users[update.user_id].username}'
        
    # # Отправляем гифку с текстом о ливнувшем в чат, чтоб все знали гада
    # await context.bot.send_animation(
    #     chat_id=chat_id, 
    #     animation='CgACAgQAAxkBAAIMZ2ViEt_jrL0C5RC7OpWLCudn7dauAAIsAwAC_IYFU-jzM0htsPhlHgQ', 
    #     caption=text
    # )
        
    
@on_message(group=301)
async def check_gold_rain(update, context):
    '''Отправляет редкое сообщение с золотым Поднебесным'''
    message = update.message
    
    if random.random() < rare_chance:  
        await context.bot.send_video(
            chat_id=message.chat.id,
            video='./service/assets/gold_rain.mp4',
            caption='ВЫ ПОЙМАЛИ РЕДКОГО ДАУНА',
            reply_to_message_id=message.message_id,
            has_spoiler=True,
        )
        
        # Останавливаем отслеживание сообщения другими хендлерами
        raise ApplicationHandlerStop
        
        
@on_message(filters.TEXT, group=302)
async def check_khaleesi(update, context):
    '''Отправляет редкое сообщение с перекривлянием'''
    message = update.message
    
    if random.random() < rare_chance: 
        khaleesi_text = Khaleesi.khaleesi(message.text)
        await message.reply_text(text=khaleesi_text.upper())
        
        # Останавливаем отслеживание сообщения другими хендлерами
        raise ApplicationHandlerStop
        
        
@on_message(filters.Regex('/dick@Dickfindbot'), group=303)
async def check_dickbot(update, context):
    '''Отправляет редкое сообщение на дикбота'''
    message = update.message
    
    if random.random() < rare_chance: 
        await message.reply_photo(photo='https://i1.sndcdn.com/artworks-J8HHeKmSxBfHO6jd-zRH7Qg-t500x500.jpg')
        
        # Останавливаем отслеживание сообщения другими хендлерами
        raise ApplicationHandlerStop
        
        
@on_message(filters.Regex('😂') | filters.Regex('🤣'), group=304)
async def check_emoji(update, context):
    '''Отправляет редкое сообщение грузовиком эмоджи'''
    message = update.message
    
    if random.random() < rare_chance: 
        await message.reply_photo(photo='./service/assets/roflmao.jpg')
        
        # Останавливаем отслеживание сообщения другими хендлерами
        raise ApplicationHandlerStop
        
        
@on_message(group=305)
async def check_wat(update, context):
    '''Отправляет редкое сообщение с упоротым хлебом'''
    message = update.message
    
    if random.random() < rare_chance:  
        await message.reply_animation(animation='CgACAgQAAxkBAAILfWVhCIKUKXltMNcFBmIZnXYIxni8AAL5AgAC9aIlU7GzxFg7V2j3HgQ')
        
        # Останавливаем отслеживание сообщения другими хендлерами
        raise ApplicationHandlerStop
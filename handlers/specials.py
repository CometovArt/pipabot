# Хэндлер предназначен для специальных, редких ответов бота

from pyrogram import filters
from pyrogram.raw.types import UpdateChannelParticipant
from config import pipabot, rare_chance, logger

import random

from utils.khaleesi import Khaleesi


@pipabot.on_deleted_messages(group=1000000)
async def check_deletes(client, message):
    logger.info(message)


@pipabot.on_message(filters.new_chat_members)
async def check_new_member(client, message):
    '''Присылает приветственный ответ новому члену чата'''
    
    await message.reply_sticker(sticker='CAACAgIAAxkBAAIH4mUjsUJPcajrLz5RQJNqDFqIF6YaAALOIQACpAABqUjNr9y1vYnsJx4E')
    
    # Останавливаем отслеживание сообщения другими хендлерами
    message.stop_propagation()
    
    
@pipabot.on_raw_update(group=1000)
async def check_left_member(client, update, users, chats) -> int:
    '''Идентифицирует ливнувшего из чата гада (работает только если у бота есть админка)'''
    
    # Ожидаем обновления UpdateChannelParticipant, оно присылается, когда изменяется состав участников чата
    if type(update) == UpdateChannelParticipant:
        chat_id = f'-100{update.channel_id}'
        
        # Проверяем есть ли виновник обновления в составе чата, потому что
        # обновление срабатывает так же при входе юзера в чат
        members = []
        async for member in pipabot.get_chat_members(chat_id):
            members.append(int(member.user.id))
            
        if int(update.user_id) in members:
            return
        
        # Собираем текстовое сообщение с инфой
        text = 'Ливнул, гад:\n\n'
        text += f'**{users[update.user_id].first_name}** '
        
        if users[update.user_id].last_name:
            text += f'**{users[update.user_id].last_name}**'
            
        if users[update.user_id].username:
            text += f'\n@{users[update.user_id].username}'
            
        # Отправляем гифку с текстом о ливнувшем в чат, чтоб все знали гада
        await pipabot.send_animation(
            chat_id=chat_id, 
            animation='CgACAgQAAxkBAAIMZ2ViEt_jrL0C5RC7OpWLCudn7dauAAIsAwAC_IYFU-jzM0htsPhlHgQ', 
            caption=text
        )
        
    
@pipabot.on_message(group=301)
async def check_gold_rain(client, message):
    '''Отправляет редкое сообщение с золотым Поднебесным'''
    
    if random.random() < rare_chance:  
        await pipabot.send_video(
            chat_id=message.chat.id,
            video='./service/assets/gold_rain.mp4',
            caption='ВЫ ПОЙМАЛИ РЕДКОГО ДАУНА',
            has_spoiler=True,
            reply_to_message_id=message.id
        )
        
        # Останавливаем отслеживание сообщения другими хендлерами
        message.stop_propagation()
        
        
@pipabot.on_message(filters.text, group=302)
async def check_khaleesi(client, message):
    '''Отправляет редкое сообщение с перекривлянием'''
    
    if random.random() < rare_chance: 
        khaleesi_text = Khaleesi.khaleesi(message.text)
        await message.reply_text(text=khaleesi_text.upper())
        
        # Останавливаем отслеживание сообщения другими хендлерами
        message.stop_propagation()
        
        
@pipabot.on_message(filters.regex('/dick@Dickfindbot'), group=303)
async def check_dickbot(client, message):
    '''Отправляет редкое сообщение на дикбота'''
    
    if random.random() < rare_chance: 
        await message.reply_photo(photo='https://i1.sndcdn.com/artworks-J8HHeKmSxBfHO6jd-zRH7Qg-t500x500.jpg')
        
        # Останавливаем отслеживание сообщения другими хендлерами
        message.stop_propagation()
        
        
@pipabot.on_message(filters.regex('😂') | filters.regex('🤣'), group=304)
async def check_emoji(client, message):
    '''Отправляет редкое сообщение грузовиком эмоджи'''
    
    if random.random() < rare_chance: 
        await message.reply_photo(photo='./service/assets/roflmao.jpg')
        
        # Останавливаем отслеживание сообщения другими хендлерами
        message.stop_propagation()
        
        
@pipabot.on_message(group=305)
async def check_wat(client, message):
    '''Отправляет редкое сообщение с упоротым хлебом'''
    
    if random.random() < rare_chance:  
        await message.reply_animation(animation='CgACAgQAAxkBAAILfWVhCIKUKXltMNcFBmIZnXYIxni8AAL5AgAC9aIlU7GzxFg7V2j3HgQ')
        
        # Останавливаем отслеживание сообщения другими хендлерами
        message.stop_propagation()
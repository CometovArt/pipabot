# Хэндлер предназначен для ответов бота с помощью нейросети

from pyrogram import filters, enums
from config import pipabot, logger
from tokens import openai_key_list

import re
import asyncio
import openai



@pipabot.on_message(
    filters=(
    filters.regex('[пПpP][иИiI][пПpP][аАыЫуУaA]') & filters.regex('\?') & ~filters.reply
    | filters.regex('[пПpP][иИiI][пПpP][аАыЫуУaA][,\s]? [оО][тТ][вВ][еЕ][тТ][ьЬ]') & ~filters.reply 
    | filters.regex('[пПpP][иИiI][пПpP][аАыЫуУaA][,\s]? [вВ][оО][пП][рР][оО][сС]') & ~filters.reply
    | filters.regex('[пПpP][иИiI][пПpP][аАыЫуУaA][,\s]? [сС][кК][аА][жЖ][иИ]') & ~filters.reply 
    | filters.regex('[пПpP][иИiI][пПpP][аАыЫуУaA][,\s]? [пП][рР][иИ][дД][уУ][мМ][аА][йЙ]') & ~filters.reply 
    | filters.regex('[пПpP][иИiI][пПpP][аАыЫуУaA][,\s]? [рР][аА][сС][сС][кК][аА][жЖ][иИ]') & ~filters.reply
    | filters.regex('[пПpP][иИiI][пПpP][аАыЫуУaA][,\s]? [пП][рР][оО][дД][оО][лЛ][жЖ][иИ]') & ~filters.reply))
async def openai_answer(client, message):
    '''
    Отвечает на вопрос с помощью нейронки
    
    Принимает запросы двух видов: 
    
        — пипа <запрос> ? \n
        — пипа [слово триггер] <запрос>
    '''
    
    # Передаём нейронке сам запрос с текстом пользователя. 
    # Понижение регистра немного уменьшает ошибки при ответе, хз почему
    user_text = message.text.lower()

    # Получаем ответ от нейронки
    text = await openai_response(message=message, promt=user_text)

    # Отправляем ответ юзеру, предварительно
    await message.reply_text(text.upper())
    
    # Останавливаем отслеживание сообщения другими хендлерами
    message.stop_propagation()
    

@pipabot.on_message(filters.regex('\?') & filters.reply & ~filters.regex('[пПpP][иИiI][пПpP][аАыЫуУaA]') | filters.regex('[пП]родолжи') & filters.reply)
async def openai_reply(client, message):
    '''Отвечает на вопрос с помощью нейронки, если это реплай боту. Учитывает контекст сообщения в реплае'''

    # Игнорируем сообщение, если реплай сделан не боту
    if message.reply_to_message.from_user != await pipabot.get_me():
        return
    
    # Передаём нейронке контекст из предыдущего сообщения
    # Чтобы уменьшить ошибки при ответе убираем все строки из сообщения
    context = re.sub(r'\n', ' ', message.reply_to_message.text or message.reply_to_message.caption)
    
    # Передаём нейронке сам запрос с текстом пользователя
    # Понижение регистра немного уменьшает ошибки при ответе
    user_text = message.text.lower()
    
    # Получаем ответ от нейронки
    text = await openai_response(message, context=context.lower(), promt=user_text)

    # Отправляем ответ юзеру, предварительно
    await message.reply_text(text.upper())
    
    # Останавливаем отслеживание сообщения другими хендлерами
    message.stop_propagation()
    
    
@pipabot.on_message(filters.regex('[пПpP][иИiI][пПpP][аАыЫуУaA]') & filters.regex('\?') & filters.reply)
async def openai_reply_pipa(client, message):
    '''Отвечает на вопрос с помощью нейронки, если это реплай с упоминанием Пипы. Учитывает контекст сообщения в реплае'''
    
    # Передаём нейронке контекст из предыдущего сообщения
    # Чтобы уменьшить ошибки при ответе убираем все строки из сообщения
    context = re.sub(r'\n', ' ', message.reply_to_message.text or message.reply_to_message.caption)
    
    # Передаём нейронке сам запрос с текстом пользователя
    # Понижение регистра немного уменьшает ошибки при ответе
    user_text = message.text.lower()
    
    # Получаем ответ от нейронки
    text = await openai_response(message, context=context.lower(), promt=user_text)

    # Отправляем ответ юзеру, предварительно
    await message.reply_text(text.upper())
    
    # Останавливаем отслеживание сообщения другими хендлерами
    message.stop_propagation()
    
    
async def openai_response(message, context=None, promt=None):
    '''Отправляет запрос в OpenAI'''
    
    # Задаём пипе характер с помощью препромта
    prepromt = 'Ответь так, как будто ты персонаж PIPA, который немного туповат и пытается пошутить: '
    
    # Отправляем в чат «PIPA печатает...»
    await pipabot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    
    # Задаём дэфолтный выбор openai ключа из списка
    # Когда будем получать ошибку RateLimitError ключ будет меняться
    key_choice = 0
    
    # Запускаем цикл для получения ответа от openai
    # Цикл нужен, чтобы при упоре во все ограничения сообщение юзера не пропадало,
    # а бот в любом случае дожидался ответа от нейросети
    response = None
    while response is None:
        try:
            openai.api_key = openai_key_list[key_choice]
            
            # Пробуем получить ответ от openai
            # Модель text-davinci-003 лучше всего подходит для тупых ответов PIP'ы
            response = openai.Completion.create(
                model='text-davinci-003',
                prompt=prepromt + context if context else '' + promt,
                temperature=0, 
                max_tokens=500
            )
            
            # Вытаскием текст из респонза
            text = response.choices[0].text.upper()
            
            # Иногда text-davinci-003 отвечает пустым текстовым полем
            # Пробуем получить ответ без контекста
            if text == '':
                response = openai.Completion.create(
                    model='text-davinci-003',
                    prompt=prepromt + promt,
                    temperature=0, 
                    max_tokens=500
                )
                
                # Вытаскием текст из респонза
                text = response.choices[0].text.upper()
            
            # Если и с контекстом нейросеть отдаёт пустой результат, то
            # чтобы не скипать сообщение пробуем получить ответ через 3.5
            if text == '':
                response = await openai.ChatCompletion.acreate(
                    model='gpt-3.5-turbo',
                    temperature=1, 
                    messages=[{ 'role':'user','content' : prepromt + context if context else '' + promt}],
                    max_tokens=500
                )
                
                # Вытаскием текст из респонза
                text = response.choices[0].message.content
            
        except openai.error.RateLimitError:
            # Получив ошибку меняем ключ для следующего цикла
            key_choice += 1
            
            # Если все ключи перебраны, то ждём 30 секунд и начинаем сначала
            if key_choice > 4:
                await asyncio.sleep(10)
                await pipabot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
                await asyncio.sleep(10)
                await pipabot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
                await asyncio.sleep(10)
                await pipabot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
                key_choice = 0
                
    # Иногда нейросеть дописывает к запросу знаки, непонятно зачем. Убираем
    if text[0] == '?' or text[0] == '!':
        text = text[3:]
    
    return text
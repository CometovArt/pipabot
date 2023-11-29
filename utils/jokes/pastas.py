# Утилита для парсинга паст

from config import userbot, morph
import random



async def get_pasta():
    '''Парсит случайную пасту с телеграм канала @myfavoritejumoreski'''
    
    # Запускаем цикл для получения пасты
    # Цикл проходит по случайным id сообщений из канала, пока получит сообщение без ошибки
    joke = None
    while joke == None:
        random_number = random.randint(1, 15756)
        message = await userbot.get_messages('@myfavoritejumoreski', random_number)
        
        # Забираем шутку, если она текстовая, чтобы избежать ненужной выдачи
        if message.text:
            joke = message.text
    
    return joke
            
            
async def get_pasta_pro(pasta_result):
    '''Ищет случайную пасту по тексту юзера с телеграм канала @myfavoritejumoreski'''
    
    # Генерируем набор склонений из запроса
    try:
        words = [
            morph.parse(pasta_result)[0].normal_form,
            morph.parse(pasta_result)[0].inflect({'gent'}).word,
            morph.parse(pasta_result)[0].inflect({'datv'}).word,
            morph.parse(pasta_result)[0].inflect({'accs'}).word,
            morph.parse(pasta_result)[0].inflect({'ablt'}).word,
            morph.parse(pasta_result)[0].inflect({'loct'}).word
        ]
    except AttributeError:
        words = [pasta_result]
    
    # Телеграм умеет сам работать со склонениями, но не всегда это работает
    # Чтобы пофиксить недостатки телеги создаём цикл по склонениям, если
    # изначальный результат телеги был кривой
    for word in words:
        pasta_list = []
        async for find_message in userbot.search_messages('@myfavoritejumoreski', query=word):
            if find_message.text:
                pasta_list.append(find_message.text)
                
        # Если нашли сообщения по первичной выдаче телеги, то выбираем случайное и отправляем юзеру
        # В противном случае крутим цикл дальше
        if pasta_list != []:
            pasta = random.choice(pasta_list)
            return pasta
    
    # # Если по окончанию цикла не нашли ни одной пасты, то отправляем юзеру печальку
    # answers = ['Я, КОНЕЧНО, ТУПОЙ РОБОТ, НО ТАКОЙ ХУЙНИ ДАЖЕ Я НАЙТИ НЕ МОГУ', 'НУ НЕ ЗНАЮ Я ТАКОЙ ПАСТЫ, НЕ ЗНА Ю', '🤨']
    # choise_answer = random.choice(answers)
    choise_answer = None
    
    return choise_answer
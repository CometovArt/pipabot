# Утилита для парсинга квна

from aiohttp import ClientSession
from bs4 import BeautifulSoup
import sqlite3 as sl
import random
import re

from config import morph



async def get_kvn_juri():
    '''Парсит случайную реплику жюри с сайта kvnru.ru'''
    
    # kvnru.ru/txt.php прям на главной генерирует случайную фразу, 
    # поэтому мы просто получаем страницу и вытаскием див с текстом
    async with ClientSession(trust_env=True) as session:
        async with session.get("http://kvnru.ru/txt.php", ssl=False) as response:
            html = await response.text()
            soup = BeautifulSoup(html, "lxml")
            p_tag = soup.find('p')
            
    return p_tag.get_text()
        
        
async def get_kvn():
    '''Парсит случайную квновскую шутку из базы данных'''
    # Все шутки были заранее спаршены с сайта https://kvn.ru/jokes
    
    # Подключаемся к базе данных
    conn = sl.connect('./service/pipa.db')
    cur = conn.cursor()

    # Сортируем строки и получаем id последней, чтобы знать сколько их
    cur.execute("""SELECT joke_id FROM kvn ORDER BY joke_id DESC LIMIT 1""")
    result_joke_id, = cur.fetchone()

    # Случайно выбираем строку с шуткой
    random_number = random.randint(1, result_joke_id)

    # Вытаскиваем выбранную шутку из базы данных
    cur.execute("""SELECT * FROM kvn WHERE joke_id = ?""",(random_number,))
    result_joke = cur.fetchone()
    joke_id,title,joke = result_joke
    
    # Закрываем соединение
    conn.close()
    
    return title, joke


async def get_kvn_pro(kvn_result):
    '''Ищет случайную квновскую шутку по тексту юзера из базы данных'''
    # Все шутки были заранее спаршены с сайта https://kvn.ru/jokes
    
    # Подключаемся к базе данных
    conn = sl.connect('./service/pipa.db')
    cur = conn.cursor()
    
    # Забираем из базы данных все строки
    cur.execute("""SELECT * FROM kvn""")
    result_kvn = cur.fetchall()
    
    # Закрываем соединение
    conn.close()

    # Генерируем набор склонений из запроса
    try:
        words = [kvn_result]
        
        morphs = [
            morph.parse(kvn_result)[0].normal_form,
            morph.parse(kvn_result)[0].inflect({'gent'}).word,
            morph.parse(kvn_result)[0].inflect({'datv'}).word,
            morph.parse(kvn_result)[0].inflect({'accs'}).word,
            morph.parse(kvn_result)[0].inflect({'ablt'}).word,
            morph.parse(kvn_result)[0].inflect({'loct'}).word,
            kvn_result[:-1]
        ]
        
        for word in morphs:
            if word not in words:
                words.append(word)
                
    except AttributeError:
        words = [kvn_result]
        
    # Проходим циклом по всем склонениям, проверяя есть ли слово в каждой шутке
    joke_list = []
    for word in words:

        for result_joke in result_kvn:
            joke_id,title,joke = result_joke
            
            result = re.search(word, joke.lower())
            
            # Если нашлось сообщение с шуткой, то пихаем её в список
            if result:
                joke_list.append(result_joke)
    
    # Если список шуток не пустой, то выбираем случайную и отправляем
    if joke_list != []:
        choice_joke = random.choice(joke_list)
        joke_id,title,joke = choice_joke
        
        return title, joke
    
    # Если по окончанию цикла не нашли ни одной пасты, то отправляем юзеру печальку
    answers = ['Я, КОНЕЧНО, ТУПОЙ РОБОТ, НО ТАКОЙ ХУЙНИ ДАЖЕ Я НАЙТИ НЕ МОГУ', 'НУ НЕ ЗНАЮ Я ТАКОГО КАВЭЭНА, НЕ ЗНА Ю', '🤨']
    choise_answer = random.choice(answers)
    
    return '', choise_answer
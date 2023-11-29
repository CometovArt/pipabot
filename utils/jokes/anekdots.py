# Утилита для парсинга анекдотов

from config import morph
import random
import re

from aiohttp import ClientSession
from bs4 import BeautifulSoup



async def get_anek():
    '''Парсит случайный анекдот с сайта anecdotica.ru'''
    
    # Анекдотика прям на главной генерирует случайный анекдот, 
    # поэтому мы просто получаем страницу и вытаскием див с текстом
    async with ClientSession(trust_env=True) as session:
        async with session.get("http://anecdotica.ru/", ssl=False) as response:
            html = await response.text()
            soup = BeautifulSoup(html, "lxml")
            result = soup.find_all("div", class_="item_text")[0]
            
    return result.text
        
        
async def get_anek_pro(anek_result):
    '''Ищет случайный анекдот по тексту юзера с сайта anecdotica.ru'''
    
    async with ClientSession(trust_env=True) as session:
        # Генерируем набор склонений из запроса
        try:
            words = [
                morph.parse(anek_result)[0].normal_form,
                morph.parse(anek_result)[0].inflect({'gent'}).word,
                morph.parse(anek_result)[0].inflect({'datv'}).word,
                morph.parse(anek_result)[0].inflect({'accs'}).word,
                morph.parse(anek_result)[0].inflect({'ablt'}).word,
                morph.parse(anek_result)[0].inflect({'loct'}).word
            ]
        except AttributeError:
            words = [anek_result]
            
        for word in words:
            # Переходим сразу к странице поиска, вставляя в неё наш запрос
            url = f'http://anecdotica.ru/search?mode=0&index={word}&series=0&format=0&category=0&country=0&lang=0&action=search'
            async with session.get(url, ssl=False) as response:
                html = await response.text()
                soup = BeautifulSoup(html, "lxml")
                
                # Находим результат количества страниц поиска
                result_pgmenu = soup.find_all("div", class_="pgmenu")
                
                # Если количества страниц поиска нет - то сайт вообще анекдотов не нашел
                # Если есть - значит есть что парсить
                if result_pgmenu:
                    # Смотрим, какая максимальная страница у результатов
                    result_pgmenu_result = result_pgmenu[0]
                    result_page_number = result_pgmenu_result.text.split(' ')[2].split('/')[1]
                    
                    # Если страниц поиска несколько:
                    if int(result_page_number) > 1:
                        # Получаем ссылку на страницу результатов
                        # Для каждого запроса там немного отличаются id
                        a_elements = result_pgmenu_result.find_all('a', href=True)
                        search_page_url = a_elements[1]['href']
                        
                        # Случайно выбираем страницу с анекдотами
                        random_number = random.randint(1, int(result_page_number))
                        
                        # Собираем ссылку на нужную страницу поиска
                        pattern = re.compile(r'page=(\d+)')
                        pattern_result = pattern.sub(f'page={random_number}', search_page_url)
                        new_url = 'http://anecdotica.ru/' + pattern_result

                        # И уже на этой странице получаем все шутки и выбираем случайную
                        async with session.get(new_url, ssl=False) as response:
                            html = await response.text()
                            soup = BeautifulSoup(html, "lxml")
                            result_items = soup.find_all("div", class_="item_text")
                            choise_joke = random.choice(result_items)
                            
                            return choise_joke.text
                            
                    # Если страница одна, то можем прям на ней найти все анекдоты и выбрать случайный
                    else:
                        result_items = soup.find_all("div", class_="item_text")
                        choise_joke = random.choice(result_items)
                        
                        return choise_joke.text

        # # Если по окончанию цикла не нашли ни одного анекдота, то отправляем юзеру печальку
        # answers = ['Я, КОНЕЧНО, ТУПОЙ РОБОТ, НО ТАКОЙ ХУЙНИ ДАЖЕ Я НАЙТИ НЕ МОГУ', 'НУ НЕ ЗНАЮ Я ТАКИХ АНЕКДОТОВ, НЕ ЗНА Ю', '🤨']
        # choise_answer = random.choice(answers)
        choise_answer = None
        
        return choise_answer
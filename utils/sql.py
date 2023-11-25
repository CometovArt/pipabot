# Утилита для работы с базой данных

import sqlite3 as sl
from config import logger
from pyrogram import filters



def filters_dark_side(data=True):
    async def func(flt, _, query):
        conn = sl.connect('./service/pipa.db')
        cur = conn.cursor()
        
        cur.execute("""SELECT status FROM settings WHERE title = 'dark_side' """)
        result, = cur.fetchone()
        logger.info(result)
        
        conn.close()
        
        if result:
            return False
            
        return True

    return filters.create(func, data=data)
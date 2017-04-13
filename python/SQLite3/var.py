import sqlite3
import time
import datetime
import random

con = sqlite3.connect('main.db')
cursor = con.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS var(unix REAL, dateS TEXT, keyword TEXT, value REAL)')

def entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Dhruv'
    value = random.randrange(0, 10)
    cursor.execute('INSERT INTO var (unix, dateS, keyword, value) VALUES (?, ?, ?, ?)',(unix, date, keyword, value))
    con.commit()

create_table()
for i in range(10):
    entry()
    time.sleep(1)

cursor.close()
con.close()

import sqlite3

con = sqlite3.connect('main.db')
cursor = con.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS var(unix REAL, dateS TEXT, keyword TEXT, value REAL)')

def read():
    cursor.execute('SELECT * FROM var')
    data = cursor.fetchall()
    print(data)

read()
cursor.close()
con.close()

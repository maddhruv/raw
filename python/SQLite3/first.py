import sqlite3

con = sqlite3.connect('main.db')#conenction with the db
cursor  = con.cursor()#cursor


def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS practise(unix REAL, dateS TEXT, keyword TEXT, value REAL)')

def data_entry():
    cursor.execute('INSERT INTO practise VALUES(1253, "2017:04:13", "python", 5)')
    con.commit()
    cursor.close()
    con.close()

create_table()
data_entry()

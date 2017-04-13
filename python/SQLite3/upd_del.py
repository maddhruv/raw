import sqlite3

con = sqlite3.connect('main.db')
cursor  = con.cursor()

def update():
    cursor.execute('SELECT * FROM var')

    cursor.execute('UPDATE var SET value = 99 WHERE value = 4')
    con.commit()

    [print(row) for row in cursor.fetchall()]

def delete():
    cursor.execute('SELECT * FROM var')

    cursor.execute('DELETE FROM var WHERE value = 99')
    con.commit()

    [print(row) for row in cursor.fetchall()]

delete()
#update()
cursor.close()
con.close()

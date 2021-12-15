import sqlite3
import os


def CreateDB(path_db):
    exists = os.path.isfile(path_db)
    if exists:
        pass
    else:
        try:
            # Create a database in RAM
            db = sqlite3.connect(':memory:')
            # Creates or opens a file called mydb with a SQLite3 DB
            db = sqlite3.connect(path_db)
            # Get a cursor object
            cursor = db.cursor()
            cursor.execute('''
                        CREATE TABLE libro_procesado(id INTEGER PRIMARY KEY, file TEXT, fecha_procesado TEXT) ''')
            db.commit()
        except NameError:
            print('Error al querer crear la base de datos!')


def InsertDB(path_db, file, dt):
    try:
        db = sqlite3.connect(path_db)
        cursor = db.cursor()
        cursor.execute('''INSERT INTO libro_procesado(file, fecha_procesado)VALUES(?,?)''', (file, dt))
        db.commit()
    except NameError:
        print('Error al querer insertar datos en la base de datos!')


def Select(path_db):
    db = sqlite3.connect(path_db)
    cursor = db.cursor()
    cursor.execute("SELECT file FROM libro_procesado")
    lst = []
    rows = cursor.fetchall()
    for r in rows:
        lst.append(r[0])
    return lst

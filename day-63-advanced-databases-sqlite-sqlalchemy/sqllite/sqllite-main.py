import sqlite3

db = sqlite3.connect("books-collection.db")
cursor = db.cursor()


try:
    cursor.execute(
        "CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) "
        "NOT NULL, rating FLOAT NOT NULL)")
except sqlite3.OperationalError:
    print("Table already exist")
finally:
    cursor.execute("INSERT INTO books VALUES(4, 'San Dag', 'J. K. Rowling', '7')")
    db.commit()

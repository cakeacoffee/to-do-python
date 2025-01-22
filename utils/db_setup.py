import sqlite3

def connect():
    connection = sqlite3.connect("database/todopy.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS todolist (id INTEGER, name TEXT)")
    cursor.execute("INSERT INTO todolist VALUES (1, 'alice')")
    cursor.execute("INSERT INTO todolist VALUES (2, 'bob')")
    cursor.execute("INSERT INTO todolist VALUES (3, 'eve')")
    connection.commit()
    print(connection.total_changes) #debug
    return cursor

def add_data(cursor):
    pass

def show_db(cursor):
    cursor.execute("SELECT * FROM todolist")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

if __name__ == "__main__":
    cursor = connect()
    show_db(cursor)

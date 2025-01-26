import sqlite3


def initialize_database(db_name: str):
    # Connect and create cursor
    with sqlite3.connect(f"database/{db_name}.db") as connection:
        cursor = connection.cursor()

        # Create Tables
        try:
            # Start transaction
            connection.execute("BEGIN")

            # Create
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS todolist (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT
                    )
            """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS item (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    done BOOLEAN,  -- Will be stored as INTEGER (0 or 1)
                    todolistid INTEGER,
                    FOREIGN KEY(todolistid) REFERENCES todolist(id))
            """
            )

            # Commit
            connection.commit()
        except Exception as e:

            # Rollback if there was an Issue
            connection.rollback()
            #!
            message = f"Transaction failed: {e}"
            print("debug: Transaction failed:", e)
        finally:
            connection.close()


def add_list(db_name: str, list_name: str):
    with sqlite3.connect(f"database/{db_name}.db") as connection:
        cursor = connection.cursor()

        try:
            connection.execute("BEGIN")
            cursor.execute(f"INSERT INTO todolist (name) VALUES (?)", (list_name))
            connection.commit()

            print(f"List '{list_name}' added successfully with ID {cursor.lastrowid}.")
        except Exception as e:
            connection.rollback()
            print("debug: Transaction failed:", e)
        finally:
            connection.close()


def connect():
    connection = sqlite3.connect("database/todopy.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS todolist (id INTEGER, name TEXT)")
    cursor.execute("INSERT INTO todolist VALUES (1, 'alice')")
    cursor.execute("INSERT INTO todolist VALUES (2, 'bob')")
    cursor.execute("INSERT INTO todolist VALUES (3, 'eve')")
    connection.commit()
    print(connection.total_changes)  # debug
    return cursor


def create_tables():
    connection = sqlite3.connect("database/todopy.db")
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS todolist (id INTEGER, name TEXT)")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS item (id INTEGER, name TEXT, done INTEGER, todolistid INTEGER, FOREIGN KEY(todolistid) REFERENCES todolist(id))"
    )
    connection.commit()
    print(connection.total_changes)  # debug

    cursor.execute("INSERT INTO todolist VALUES (1, 'alice')")
    cursor.execute("INSERT INTO todolist VALUES (2, 'bob')")
    cursor.execute("INSERT INTO todolist VALUES (3, 'eve')")
    connection.commit()
    print(connection.total_changes)  # debug

    cursor.execute("INSERT INTO item VALUES (1, 'apple', 0, 1)")
    cursor.execute("INSERT INTO item VALUES (2, 'pineapple', 0, 1)")
    cursor.execute("INSERT INTO item VALUES (3, 'pen', 0, 2)")
    cursor.execute("INSERT INTO item VALUES (4, 'ugh', 0, 1)")
    connection.commit()
    print(connection.total_changes)  # debug

    return cursor


def add_data(cursor):
    pass


def show_db(cursor):
    cursor.execute(
        """
        SELECT *
        FROM todolist
        JOIN item ON todolist.id = item.todolistid
    """
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    cursor = create_tables()
    show_db(cursor)

    todopy

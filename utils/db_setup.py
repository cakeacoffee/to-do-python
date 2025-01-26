import sqlite3


def initialize_database(db_name: str = "todopydb"):
    # Connect and create cursor
    message = ""  # for reporting to user

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
                    name TEXT UNIQUE
                    )
            """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS item (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    done BOOLEAN DEFAULT 0,
                    todolistid INTEGER,
                    FOREIGN KEY(todolistid) REFERENCES todolist(id))
            """
            )
            connection.commit()
            message = "Database has been set up"
        except sqlite3.Error as e:
            connection.rollback()
            message = f"Database error: {e}"
        except Exception as e:
            connection.rollback()
            message = f"Unexpected error: {e}"
        finally:
            print(message)


def add_list(list_name: str, db_name: str = "todopydb"):
    message = ""
    with sqlite3.connect(f"database/{db_name}.db") as connection:
        cursor = connection.cursor()

        try:
            connection.execute("BEGIN")
            cursor.execute(
                f"INSERT INTO todolist (name) VALUES (?)", (list_name,)
            )  # needs to be a tuple , hence trailing , to specify
            connection.commit()

            message = (
                f"List '{list_name}' added successfully with ID {cursor.lastrowid}."
            )
        except sqlite3.IntegrityError:
            connection.rollback()
            message = f"Error: The list name '{list_name}' already exists."
        except sqlite3.Error as e:
            connection.rollback()
            message = f"Database error: {e}"
        except Exception as e:
            connection.rollback()
            message = f"Unexpected error: {e}"
        finally:
            print(message)


def add_item(item_name: str, list_name: str, db_name: str = "todopydb"):
    message = ""
    with sqlite3.connect(f"database/{db_name}.db") as connection:
        cursor = connection.cursor()

        try:
            connection.execute("BEGIN")

            # Get the id of the to-do list by name
            cursor.execute("SELECT id FROM todolist WHERE name = ?", (list_name,))
            result = cursor.fetchone()
            if not result:
                raise ValueError(f"list:'{list_name}' not found.")
            todolist_id = result[0]

            # insert
            cursor.execute(
                "INSERT INTO item (name, todolistid) VALUES (?, ?)",
                (item_name, todolist_id),
            )

            # add link to todolist table
            connection.commit()

            message = f"Item '{item_name}' added to the to-do list '{list_name}'."
        except sqlite3.IntegrityError:
            connection.rollback()
            message = f"Error: The list name '{list_name}' already exists."
        except sqlite3.Error as e:
            connection.rollback()
            message = f"Database error: {e}"
        except Exception as e:
            connection.rollback()
            message = f"Unexpected error: {e}"
        finally:
            print(message)


def show_db(db_name: str = "todopydb"):
    with sqlite3.connect(f"database/{db_name}.db") as connection:
        cursor = connection.cursor()

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
    db_name = "freshdb"
    initialize_database(db_name)
    add_list("alice", db_name)
    add_list("bob", db_name)
    add_list("eve", db_name)
    add_item("apple", "alice", db_name)
    add_item("pineapple", "alice", db_name)
    add_item("pen", "bob", db_name)

    show_db(db_name)

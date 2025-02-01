import sqlite3


def initialize_database(db_name: str = "todopydb") -> str:
    """### Initialise the database

    * Create `todolist` table and `item` table

    Args:
        `db_name (str, optional): the database. defaults to "todopydb"`

    Returns:
        `str: message, for cli output`
    """
    message = ""

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

    return message


def validate_str(string: str) -> bool:
    """### Validate a String
    * check if string is empty and is a string

    Args:
        `string (str): the string to be validated`

    Raises:
        `ValueError: non empty string error`
        `ValueError: empty and white space error`

    Returns:
        `bool: true if passes checks`
    """
    if not isinstance(string, str):
        raise ValueError("Name must be a non-empty string")
    if len(string.strip()) == 0:
        raise ValueError("Name cannot be empty or just whitespace.")
    return True


def add_list(list_name: str, db_name: str = "todopydb") -> str:
    """### Add a new list

    Args:
        `list_name (str): the list name`
        `db_name (str, optional): the database. defaults to "todopydb"`

    Returns:
        `str: message, for cli output`
    """
    message = ""
    try:
        validate_str(list_name)

        with sqlite3.connect(f"database/{db_name}.db") as connection:
            cursor = connection.cursor()
            connection.execute("BEGIN")
            cursor.execute(
                f"INSERT INTO todolist (name) VALUES (?)", (list_name,)
            )  # needs to be a tuple , hence trailing , to specify
            connection.commit()

            message = (
                f"List '{list_name}' added successfully with ID {cursor.lastrowid}."
            )

    except ValueError as ve:
        message = f"Validation error: {ve}"
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
        return message


def add_item(item_name: str, list_name: str, db_name: str = "todopydb") -> str:
    """### Add new Item

    Args:
        `item_name (str): the item name`
        `list_name (str): _list to add to`
        `db_name (str, optional): the database. Defaults to "todopydb".`

    Raises:
        `ValueError: not found list name error`

    Returns:
        `str: message, for cli output`
    """
    message = ""
    try:
        validate_str(item_name)

        with sqlite3.connect(f"database/{db_name}.db") as connection:
            cursor = connection.cursor()

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

            message = (
                f"Item '{item_name}' added to the to-do list '{list_name}'."
            )
    except ValueError as ve:
        message = f"Validation error: {ve}"
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
        return message


def show_db(db_name: str = "todopydb"):
    #!debug
    with sqlite3.connect(f"database/{db_name}.db") as connection:
        cursor = connection.cursor()

        #cursor.execute(
        """
            SELECT *
            FROM todolist
            JOIN item ON todolist.id = item.todolistid
        """
        #)
        
        #cursor.execute(
        """
            SELECT *
            FROM todolist
        """
        #)
        cursor.execute(
            """
            SELECT *
            FROM item
            """
        )

    rows = cursor.fetchall()
    for row in rows:
        print(row)


if __name__ == "__main__":
    db_name = "todopydb"
    """
    initialize_database(db_name)
    add_list("steven", db_name)
    add_list("bob", db_name)
    add_list("eve", db_name)
    add_item("apple", "alice", db_name)
    add_item("pineapple", "alice", db_name)
    add_item("pen", "bob", db_name)
    """
    show_db(db_name)

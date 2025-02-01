# Learnings
This document is for documenting things i learnt (both big and small) from this project. This is primarily as a personal note.  

## Python
### Comprehensions
python for loops can be simplified using comprehensions, discussed in [this blog post](https://blog.teamtreehouse.com/python-single-line-loops).
> Comprehensions are constructs that allow you to generate a new collection in a concise, readable way by embedding loops and conditional logic directly within the collection’s definition. The most commonly used comprehension is the list comprehension, but similar constructs exist for dictionaries, sets, and generators.

**Example**
```python
[expression for item in iterable]
```
Rather than having a regular for loop to add each item to the dictionary, comprehension can be used. For example in the file `to_do_list.py`
``` python
def to_dict(self):
    return {
        "name": self.name,
        "items": [{"item": item.name, "done": item.done} for item in self.items],
    }
```

## SQLite 
### No Bool
SQLite does not have the boolean storage class, [as stated in the SQLite Documentation](https://www.sqlite.org/datatype3.html). SQLite will stor the values as integers of 0 and 1.
* The key word `BOOLEAN` can still be used.
* The keywords "True" and "False" are recognised

**Additional Note**
> REMEMBER: strings are slower than integers and take more space, so use int

### Auto increment id
`AUTOINCREMENT` can be used to increase each new record added. this is useful for incrementing id

**EXAMPLE** from `db_setup.py`
``` sql
CREATE TABLE IF NOT EXISTS todolist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
```
### SQL Injection
[SQL Injection](https://www.w3schools.com/sql/sql_injection.asp) is a code injection technique that might destroy a database. Its best practice to prevent this.

[more info](https://learn.snyk.io/lesson/sql-injection/)

simple solution is to insert data safely with ? placeholders.

**EXAMPLE**

`cursor.execute(f"INSERT INTO todolist (name) VALUES (?)", (list_name))`

### SQL EXAMPLE

```SQL
CREATE TABLE IF NOT EXISTS item (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    done BOOLEAN DEFAULT 0,  -- Default is 'False' (0) -- Will be stored as INTEGER (0 or 1)
    todolistid INTEGER,
    FOREIGN KEY(todolistid) REFERENCES todolist(id)
)
```
This creates the table `item` if it currently does not exist. It has a primary key id that automaticly increments the integer id `+1` when a new item is added. has test attribute called `name`. An attribute called `done` that will be stored as an integer (labeled as boolean) and defaults to 0 (`false`). It also links to the `todolist` table via `todolistid` `FOREIGN KEY`.

**EXAMPLE**
```sql
CREATE TABLE primary_table(
    ...
    fk_att_name INTEGER,
    FOREIGN KEY(fk_att_name) REFERENCES foreign_table(id)
)
```
## Validation
Data should be validated before interacting with the database to ensure that it meets the necessary constraints and formats
examples

## Exception Handling
> improving my exception handling to catch different types of errors and provide clear feedback to the user. 

Exceptions can be broken down based on the specific issues that may occur.

**EXAMPLE**

IntegrityError

* This occurs if there's a unique constraint violation (e.g., trying to add a duplicate name)

ValueError

* For invalid or unexpected data types

OperationalError

* For database issues like bad SQL syntax or a broken connection

[more info](https://www.w3schools.com/python/python_try_except.asp)

## Database debugging
I encountered an issue where the items were not adding to the db. 
used sqlite to help debug
```bash
sudo apt install sqlite3  # For Debian/Ubuntu-based systems
```
```bash
sqlite3 database_name.db
```
```sql
.tables
```
```sql
.schema table_name
```
```sql
-- Enable column formatting for readability
.mode column
.headers on
s
-- Example: Select all rows from a table
SELECT * FROM table_name;
```
```sql
.output dump.sql  -- Redirect output to a file
.dump             -- Export the database
.quit             -- Exit SQLite CLI
```
## Reduce complexity
By cutting out the step where the CLI creates a ToDoList object, the process is simplified and made it easier to follow! Before, the app had to build an object just to pass data to the database, for a simple project like this, this is unnecessary complexity adds extra work and potential errors. Now, the CLI takes user input, checks it, and sends it straight to the database. This means fewer parts to maintain.
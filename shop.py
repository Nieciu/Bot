import sqlite3

db = sqlite3.connect("database.db")
c = db.cursor()

nameset = ['Wyrdwood Planks', 'Wyrdwood', 'Lumber', 'Obsidian Sandpaper']

create_table_items = '''
CREATE TABLE IF NOT EXISTS items (
    name text PRIMARY KEY
)
'''

create_table_recipes = '''
CREATE TABLE IF NOT EXISTS recipes (
    id integer PRIMARY KEY,
    item_name text NOT NULL,
    FOREIGN KEY (item_name) REFERENCES items (name)
    )
'''

create_table_ingredients = '''
CREATE TABLE IF NOT EXISTS ingredients (
    id integer PRIMARY KEY,
    item_name text NOT NULL,
    amount integer NOT NULL,
    FOREIGN KEY (item_name) REFERENCES items (name)
    )
'''

def insert_into_items(data):
    commander = ""
    for name in data:

        c.execute(f'''INSERT INTO items(name) VALUES("{name}");''')


    return commander[:-2]

def insert_into_recipes(data):
    c.execute(f'''INSERT INTO recipes(name) VALUES("");''')


def initialize_db():
    c.execute(create_table_items)
    c.execute(create_table_recipes)
    c.execute(create_table_ingredients)
    insert_into_items(nameset)


initialize_db()

db.commit()

db.close()
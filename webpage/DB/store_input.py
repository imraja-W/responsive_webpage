import sqlite3

# Connect to or create a database file
conn = sqlite3.connect('DB/my_database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store your inputs (if not exists)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS user_inputs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        input_text TEXT
    )
''')

# Get input from the user
user_input = input("Enter something: ")

# Insert the input into the database
cursor.execute('INSERT INTO user_inputs (input_text) VALUES (?)', (user_input,))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Input stored successfully!")

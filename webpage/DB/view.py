import sqlite3
import os

# Get the current script's directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Ensure the 'DB' folder exists
db_folder_path = os.path.join(current_dir, 'DB')
if not os.path.exists(db_folder_path):
    os.makedirs(db_folder_path)
    print(f"Created 'DB' folder")

# Connect to or create a database file in the DB folder
db_file_path = os.path.join(db_folder_path, 'my_database.db')

try:
    conn = sqlite3.connect(db_file_path)
    cursor = conn.cursor()

    # Fetch and print data from user_inputs table
    cursor.execute('SELECT * FROM user_inputs')
    data = cursor.fetchall()
    print("Data in user_inputs table:")
    for row in data:
        print(row)

except sqlite3.Error as e:
    print(f"SQLite error: {e}")

finally:
    if conn:
        conn.close()
        print("Connection closed")

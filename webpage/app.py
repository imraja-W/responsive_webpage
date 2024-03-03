from flask import Flask, render_template, request, redirect, url_for, g
import sqlite3
import os

app = Flask(__name__)

# Configuration
app.config['DATABASE'] = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'DB', 'my_database.db')
app.config['SECRET_KEY'] = 'your_secret_key'

# Initialize database
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

# Connect to the database
def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = sqlite3.connect(app.config['DATABASE'])
        g.sqlite_db.row_factory = sqlite3.Row
    return g.sqlite_db

# Close database connection when the application context ends
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

# Function to fetch data from the database
def get_data():
    db = get_db()
    cursor = db.execute('SELECT * FROM user_inputs')
    data = cursor.fetchall()
    return data

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_input = request.form['user_input']

    db = get_db()
    db.execute('INSERT INTO user_inputs (input_text) VALUES (?)', (user_input,))
    db.commit()

    return redirect(url_for('home'))

@app.route('/view')
def view():
    data = get_data()
    return render_template('view.html', data=data)

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('video_games.db')
    conn.row_factory = sqlite3.Row  # Allow accessing columns by name
    return conn

# Route to display data from the database
@app.route('/')
def index():
    conn = get_db_connection()
    data = conn.execute('SELECT * FROM VideoGame').fetchall()  # Replace 'your_table' with your actual table name
    conn.close()
    return render_template('index.html', data=data)



if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('video_games.db')
    conn.row_factory = sqlite3.Row  # Allow accessing columns by name
    return conn


# Route to display data from the database
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    data = conn.execute('SELECT * FROM VideoGame').fetchall()
    cursor.execute("SELECT * FROM VideoGame LIMIT 0") 
    column_names = [description[0] for description in cursor.description]

    conn.close()
    return render_template('index.html', data=data, columns=column_names)

@app.route('/submit', methods=['POST'])
def submit():
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        text_input = request.form['text_input']
        try:
            data = conn.execute('SELECT * FROM ' + text_input).fetchall()
            cursor.execute("SELECT * FROM " + text_input + " LIMIT 0") 
            column_names = [description[0] for description in cursor.description]
            return render_template('index.html', data=data, columns=column_names)
        except sqlite3.OperationalError:
            print("table not found")
            data = conn.execute('SELECT * FROM VideoGame').fetchall()
            cursor.execute("SELECT * FROM VideoGame LIMIT 0") 
            column_names = [description[0] for description in cursor.description]
            return render_template('index.html', data=data, columns=column_names, error_message="Table Not Found.")

        

if __name__ == '__main__':
    app.run(debug=True)
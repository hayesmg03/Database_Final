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
    data = conn.execute('SELECT * FROM Developer').fetchall()  
    conn.close()
    return render_template('index.html', data=data)

@app.route('/submit', methods=['POST'])
def submit():
    conn = get_db_connection()
    if request.method == 'POST':
        text_input = request.form['text_input']
        # Process the text input here
        data = conn.execute('SELECT * FROM ' + text_input)
        return render_template('index.html', data=data)

        

if __name__ == '__main__':
    app.run(debug=True)
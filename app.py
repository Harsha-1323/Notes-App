from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

app = Flask(__name__)
DB_PATH = 'notes.db'

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY, content TEXT)')

@app.route('/')
def index():
    with sqlite3.connect(DB_PATH) as conn:
        notes = conn.execute('SELECT * FROM notes').fetchall()
    return render_template('index.html', notes=notes)

@app.route('/add', methods=['POST'])
def add():
    content = request.form['content']
    if content.strip():
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute('INSERT INTO notes (content) VALUES (?)', (content,))
    return redirect(url_for('index'))

@app.route('/delete/<int:note_id>')
def delete(note_id):
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('DELETE FROM notes WHERE id = ?', (note_id,))
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)


from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

def create_database():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE users
                 (ID INT PRIMARY KEY     NOT NULL,
                 userName           TEXT    NOT NULL,
                 Password            TEXT     NOT NULL);''')
    conn.commit()
    conn.close()
    return 'Database created successfully!'

def query():
    conn = sqlite3.connect('mydatabase.db')
    c = conn.cursor()
    c.execute('SELECT * FROM users')
    rows = c.fetchall()
    conn.close()
    return render_template('./templates/index.html', rows=rows)


if __name__ == '__index__':
    app.run()
from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('DB_NAME', 'movies_database')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', '1818')

def get_db_connection():
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD
    )
    return conn

@app.route('/')
def hello_world():
    return 'Welcome to the Interactive Movies Comparison and Recommendation System!'

@app.route('/movies')
def list_movies():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('SELECT title, director, year FROM movies;')
    movies = cur.fetchall()
    cur.close()
    conn.close()

    movies_list = [{'title': movie[0], 'director': movie[1], 'year': movie[2]} for movie in movies]
    return jsonify(movies_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)



from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('airports.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/airport/<icao>')
def get_airport_info(icao):

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT name, location FROM airport WHERE icao = ?", (icao.upper(),))
    row = cursor.fetchone()

    conn.close()

    if row:
        return jsonify({
            "ICAO": icao.upper(),
            "Name": row['name'],
            "Location": row['location']
        })
    else:
        return jsonify({"error": "Airport not found"})


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=5000)

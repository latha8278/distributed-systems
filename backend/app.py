from flask import Flask, request, jsonify
import psycopg2
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='app.log', level=logging.DEBUG)

def get_db_connection():
    conn = psycopg2.connect(
        host="34.27.231.132",
        database="postgres",
        user="postgres",
        password="Rakesh@12345"
    )
    return conn

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    value1 = data['value1']
    value2 = data['value2']

    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO data (value1, value2) VALUES (%s, %s)', (value1, value2))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({'status': 'success'}), 200
    except Exception as e:
        logging.error(f"Error inserting data: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

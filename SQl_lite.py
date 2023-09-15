import sqlite3
from flask import Flask, jsonify, request, g

app = Flask(__name__)

# Path to your SQLite database file
DATABASE = 'mytrain.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row  # This line is important for returning rows as dictionaries
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


class Customer:
    def __init__(self, id, first_name, last_name):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name


class Track:
    def __init__(self, id, name, duration):
        self.id = id
        self.name = name
        self.duration = duration


# Route for getting unique names
@app.route('/names/', methods=['GET'])
def unique_names():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT DISTINCT first_name FROM customer")
    unique_customer_names = cursor.fetchall()
    names = [name['first_name'] for name in unique_customer_names]
    return jsonify(names)


# Route for getting customers with optional filtering
@app.route('/customers/', methods=['GET'])
def get_customers():
    filter_param = request.args.get('filter', None)
    db = get_db()
    cursor = db.cursor()
    if filter_param:
        cursor.execute("SELECT * FROM customer WHERE first_name LIKE ?", ('%' + filter_param + '%',))
    else:
        cursor.execute("SELECT * FROM customer")
    customers = [{'id': customer['id'], 'first_name': customer['first_name'], 'last_name': customer['last_name']} for customer in cursor.fetchall()]
    return jsonify(customers)


# Route for getting the count of tracks
@app.route('/tracks/count', methods=['GET'])
def track_count():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM track")
    track_count = cursor.fetchone()[0]
    return jsonify({'count': track_count})


# Route for getting track duration data
@app.route('/tracks/duration', methods=['GET'])
def track_duration():
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT name, duration FROM track")
    track_data = [{'name': track['name'], 'duration': track['duration']} for track in cursor.fetchall()]
    return jsonify(track_data)


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, jsonify, request
from faker import Faker
import csv
import requests

r = requests.get('https://api.github.com/repos/psf/requests')

r.json()["description"]

app = Flask(__name__)


# 1. Повернення вмісту файлу requirements.txt
@app.route('/requirements', methods=['GET'])
def get_requirements():
    try:
        with open('requirements.txt', 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return "File 'requirements.txt' not found.", 404


# 2. Виведення 100 випадково згенерованих юзерів
@app.route('/generate-users', methods=['GET'])
def generate_users():
    try:
        num_users = int(request.args.get('num', 100))
        fake = Faker()
        users = [{'email': fake.email(), 'name': fake.name()} for _ in range(num_users)]
        return jsonify(users)
    except ValueError:
        return "Invalid 'num' query parameter.", 400


# 3. Виведення середнього зросту та ваги з файлу hw.csv
@app.route('/mean', methods=['GET'])
def calculate_mean():
    try:
        with open('hw.csv', 'r') as file:
            csv_reader = csv.DictReader(file)
            heights = []
            weights = []
            for row in csv_reader:
                if 'Height' in row and 'Weight' in row:
                    try:
                        heights.append(float(row['Height']))
                        weights.append(float(row['Weight']))
                    except ValueError:
                        return "Invalid data in 'hw.csv'.", 500
        if heights and weights:
            avg_height = sum(heights) / len(heights)
            avg_weight = sum(weights) / len(weights)
            return jsonify({'avg_height_cm': avg_height, 'avg_weight_kg': avg_weight})
        else:
            return "No data found in 'hw.csv'.", 404
    except FileNotFoundError:
        return "File 'hw.csv' not found.", 404
    except ValueError:
        return "Invalid data in 'hw.csv'.", 500


# 4. Виведення кількості космонавтів за URL
@app.route('/space', methods=['GET'])
def get_astronauts():
    try:
        response = requests.get('http://api.open-notify.org/astros.json')
        data = response.json()
        return jsonify({'num_astronauts': data['number']})
    except requests.exceptions.RequestException as e:
        return f"Error fetching astronaut data: {str(e)}", 500


if __name__ == '__main__':
    app.run()

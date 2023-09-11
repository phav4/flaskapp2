from flask import Flask, request, jsonify

app = Flask(__name__)


def find_person_by_name(name):
    for person in persons:
        if person['name'] == name:
            return person
        return None

#       Operations


@app.route('/api/person', method=['POST'])
def create_person():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Name is requied'}), 400
    new_person = {
        'name': data['name'],
        'age': data.get('age', None)
    }

    persons.append(new_person)
    return jsonify({'message': 'person created successfully'}), 201

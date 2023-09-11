from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data as an in-memory list
persons = []

# Helper function to find a person by name


def find_person_by_name(name):
    for person in persons:
        if person['name'] == name:
            return person
    return None

# CREATE operation


@app.route('/api/person', methods=['POST'])
def create_person():
    data = request.get_json()
    if 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400
    new_person = {
        'name': data['name'],
        'age': data.get('age', None)
    }
    persons.append(new_person)
    return jsonify({'message': 'Person created successfully'}), 201

# READ operation


@app.route('/api/person/<string:name>', methods=['GET'])
def read_person(name):
    person = find_person_by_name(name)
    if person:
        return jsonify(person)
    return jsonify({'error': 'Person not found'}), 404

# UPDATE operation


@app.route('/api/person/<string:name>', methods=['PUT'])
def update_person(name):
    person = find_person_by_name(name)
    if not person:
        return jsonify({'error': 'Person not found'}), 404
    data = request.get_json()
    if 'age' in data:
        person['age'] = data['age']
    return jsonify({'message': 'Person updated successfully'})

# DELETE operation


@app.route('/api/person/<string:name>', methods=['DELETE'])
def delete_person(name):
    person = find_person_by_name(name)
    if not person:
        return jsonify({'error': 'Person not found'}), 404
    persons.remove(person)
    return jsonify({'message': 'Person deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)

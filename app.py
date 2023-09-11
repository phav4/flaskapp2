from flask import Flask, request, jsonify

app = Flask(__name__)

# data as an in-memory list
persons = []

# function to find a person by name


def find_person_by_name(name):
    for person in persons:
        if person['name'] == name:
            return person
        return None

#      Create Operations


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


#      Read Operation
@app.route('/api/person/<string:name>', method=['GET'])
def update_person(name):
    person = find_person_by_name(name)
    if person:
        return jsonify(person)
    return jsonify({'error': 'person not found'}), 404

#       Update Operation


@app.route('api/person/<string:name>', method=['PUT'])
def update_person(name):
    person = find_person_by_name(name)
    if not person:
        return jsonify({'error': 'Person not found'}), 404
    data = request.get_json()
    if 'age' in data:
        person['age'] = data['age']
        return jsonify({'message': 'Person update sucessfully'})


#       Delete Operation
@app.route('/api/person/<string:name>', method=['DELETE'])
def delete_person(name):
    person = find_person_by_name(name)
    if not person:
        return jsonify({'error': 'person not found'}), 404
    person.remove(person)
    return jsonify({'message': 'Person deleted successfully'})


if __name__ == '__main__':
    app.run(debug=True)

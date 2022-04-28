import json
import threading
import settings

from flask import Flask, jsonify, request

COUNTER_OF_DOG = {'Lera': 1,
                  'Lena': 4}

app = Flask(__name__)

@app.route('/create_user', methods=['POST'])
def create_user():
    name = json.loads(request.data)['name']
    count_dog = json.loads(request.data)['dog']

    if COUNTER_OF_DOG.get(name) is None:
        COUNTER_OF_DOG[name] = count_dog
        data = {'name': name, 'dog': count_dog}
        return jsonify(data), 200
    else:
        return jsonify(f'User {name} already exists'), 400


@app.route('/get_count_dog/<name>', methods=['GET'])
def get_user_count_dog(name):
    if dog := COUNTER_OF_DOG.get(name):
        data = {'dog': dog}
        return jsonify(data), 200
    else:
        return jsonify(f'Dog for user "{name}" not found'), 405



@app.route('/change_dog/<name>', methods=['PUT'])
def change_user_count_dog(name):
    new_dog = json.loads(request.data)['dog']
    if COUNTER_OF_DOG.get(name) is not None:
        COUNTER_OF_DOG[name] = new_dog
        data = {'name': new_dog}
        return jsonify(data), 200
    else:
        return jsonify(f'Count of dog this user cannot be changed cause the user {name} doesnt exist'), 404


@app.route('/delete_user/<name>', methods=['DELETE'])
def delete_user(name):
    if COUNTER_OF_DOG.get(name) is not None:
        COUNTER_OF_DOG.pop(name)
        return jsonify(f'User {name} was deleted successfully'), 200
    else:
        return jsonify(f'User {name} cannot be deleted because he does not exist'), 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })

    server.start()
    return server


def shutdown_stub():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_stub()
    return jsonify(f'Ok, exiting'), 200

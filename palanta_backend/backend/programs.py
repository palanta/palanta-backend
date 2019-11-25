from backend import app
from flask import request
import database
import uuid


def get_programs():
    return database.get_palanta_db().programs


def create_program(name):
    database.get_palanta_db().programs.insert_one({
        'id': uuid.uuid4().hex,
        'name': name,
    })


def delete_program(id):
    database.get_palanta_db().programs.delete_one({'id': id})


@app.route('/programs', methods=['GET', 'POST', 'DELETE'])
def programs():
    if request.method == 'GET':
        return get_programs(), 200
    elif request.method == 'POST':
        create_program(request.json['name'])
        return '', 200
    elif request.method == 'DELETE':
        delete_program(request.json['id'])
        return '', 200


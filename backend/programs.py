from backend import app
from flask import request
import database
import uuid


def get_programs():
    return database.get_palanta_db().programs


def get_program(id):
    return database.get_palanta_db().programs.find_one({'id': id})


def create_program(name):
    database.get_palanta_db().programs.insert_one({
        'id': uuid.uuid4().hex,
        'name': name,
    })


def delete_program(id):
    database.get_palanta_db().programs.delete_one({'id': id})


@app.route('/programs', methods=['GET', 'POST'])
def programs():
    if request.method == 'GET':
        return get_programs()
    if request.method == 'POST':
        create_program(request.json['name'])
        return ''


@app.route('/programs/<id>', methods=['GET', 'DELETE'])
def program(id):
    if request.method == 'GET':
        return get_program(id)
    if request.method == 'DELETE':
        return delete_program(id)


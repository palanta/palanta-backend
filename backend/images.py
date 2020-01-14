from flask import request, send_file

from . import app
from . import image_manager


@app.route('/images', methods=['POST'])
def upload():
    if len(request.files) != 1:
        return 'invalid_file_count', 400
    file = list(request.files.values())[0].filename
    print(file)
    image_id = image_manager.upload(file)
    if image_id is None:
        return 'internal_server_error', 500
    return image_id, 200


@app.route('/images/<image_id>')
def images(image_id):
    if not image_manager.exists(image_id):
        return 'not_found', 404
    return send_file(image_manager.get_path_from_id(image_id))

from flask import request, send_file

from . import app
from . import image_manager

UPLOAD_FOLDER = './tmp/'
ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png', 'gif', 'bmp'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/images', methods=['POST'])
def upload():
    if len(request.files) != 1:
        return 'invalid_file_count', 400
    file = list(request.files.values())[0]
    if file.filename == '':
        return 'no_selected_file', 400
    if not allowed_file(file.filename):
        return 'unsupported_extension', 400
    image_id = image_manager.upload(file)
    if image_id is None:
        return 'internal_server_error', 500
    return image_id, 200


@app.route('/images/<image_id>', methods=['GET'])
def images(image_id):
    if not image_manager.exists(image_id):
        return 'not_found', 404
    return send_file(image_manager.get_path_from_id(image_id))

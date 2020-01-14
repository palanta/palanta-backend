from flask import request

from . import app
from . import image_manager


@app.route('/metadata', methods=['GET'])
def metadata():
    image_id = request.args.get('image')
    image = image_manager.load(image_id)
    if image is None:
        return 'invalid_image', 400
    return {
        'shape': list(image.shape)
    }

from flask import request
import numpy as np

from . import app
from . import image_manager


@app.route('/binarize', methods=['GET'])
def binarize():
    image_id = request.args.get('image')
    try:
        threshold = float(request.args.get('threshold'))
    except ValueError:
        return 'invalid_threshold', 400
    image = image_manager.load(image_id)
    if image is None:
        return 'invalid_image', 400
    binarized = np.where(image > threshold * 255, 255, 0)
    return image_manager.save(binarized)

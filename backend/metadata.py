from flask import request
import numpy as np

from . import app
from . import image_manager


@app.route('/metadata', methods=['GET'])
def metadata():
    image_id = request.args.get('image')
    image = image_manager.load(image_id)
    if image is None:
        return 'invalid_image', 400
    image = image / 255.0
    return {
        'shape': list(image.shape),
        'mean': np.mean(image),
        'median': np.median(image),
        'std': np.std(image),
    }

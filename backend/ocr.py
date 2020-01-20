from flask import request
import numpy as np
import pytesseract

from . import app
from . import image_manager


@app.route('/ocr', methods=['GET'])
def ocr():
    image_id = request.args.get('image')
    image = image_manager.load(image_id)
    if image is None:
        return 'invalid_image', 400

    text = pytesseract.image_to_string(image)
    return text

from flask import request
import cv2
import numpy as np

from . import app
from . import image_manager


@app.route('/greyscale', methods=['GET'])
def greyscale():
    image_id = request.args.get('image')
    image = image_manager.load(image_id)
    if image is None:
        return 'invalid_image', 400
    image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return image_manager.save(image)


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


@app.route('/otsu', methods=['GET'])
def otsu():
    image_id = request.args.get('image')
    image = image_manager.load(image_id)
    if image is None:
        return 'invalid_image', 400
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    result, _ = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return str(result / 255.0)


@app.route('/invert', methods=['GET'])
def invert():
    image_id = request.args.get('image')
    image = image_manager.load(image_id)
    if image is None:
        return 'invalid_image', 400
    inverted = 255 - image
    return image_manager.save(inverted)


@app.route('/hsv', methods=['GET'])
def hsv():
    image_id = request.args.get('image')
    image = image_manager.load(image_id)
    if image is None:
        return 'invalid_image', 400
    try:
        h = float(request.args.get('h') or '1')
        s = float(request.args.get('s') or '1')
        v = float(request.args.get('v') or '1')
    except ValueError:
        return 'invalid_factors', 400
    
    image = cv2.cvtColor(image.astype(np.float32), cv2.COLOR_BGR2HSV)
    image = image * np.array([[[h, s, v]]])
    image = cv2.cvtColor(image.astype(np.float32), cv2.COLOR_HSV2BGR)
    return image_manager.save(image)

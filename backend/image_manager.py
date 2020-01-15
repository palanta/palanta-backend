import cv2
import hashlib
import os
import uuid

IMAGE_DIRECTORY = os.path.abspath('./images')
if not os.path.exists(IMAGE_DIRECTORY):
    os.makedirs(IMAGE_DIRECTORY)

def _hash(image):
    h = hashlib.sha1()
    h.update(image)
    return h.hexdigest()


def get_path_from_id(image_id):
    return os.path.join(IMAGE_DIRECTORY, image_id + '.jpg')


def exists(image_id):
    return os.path.exists(get_path_from_id(image_id))


def load(image_id):
    return cv2.imread(get_path_from_id(image_id))


def save(image):
    image_id = _hash(image)
    filename = get_path_from_id(image_id)
    cv2.imwrite(filename, image)
    return image_id


def upload(file):
    temp_filename = get_path_from_id(str(uuid.uuid4()))
    file.save(temp_filename)
    print('saved as ', temp_filename)
    image = cv2.imread(temp_filename)
    print('loaded as ', temp_filename)
    os.remove(temp_filename)
    if image is None:
        return None
    return save(image)

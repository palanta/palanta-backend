import numpy as np


def boolean_verifier(value):
    return type(value) is bool


def number_verifier(value):
    return type(value) is float


def string_verifier(value):
    return type(value) is str


def image_verifier(value):
    if type(value) is not np.array:
        return False
    s = value.shape
    # Require three color channels.
    return len(s) == 3 and s[-1] == 3


def bundle_verifier(element_verifier, value):
    if type(value) is not list:
        return False
    # Verify each element with the element_verifier.
    for element in value:
        if not element_verifier(element):
            return False
    return True

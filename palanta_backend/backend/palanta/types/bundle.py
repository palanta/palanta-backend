def collapse(value):
    if type(value) is not list:
        return value
    elements = []
    for e in value:
        elements.extend(collapse(e))
    return elements

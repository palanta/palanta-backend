def collapse(value):
    """Collapses nested bundles into regular bundles."""
    if type(value) is not list:
        return value
    elements = []
    for e in value:
        elements.extend(collapse(e))
    return elements

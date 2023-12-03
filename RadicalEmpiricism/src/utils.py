

def is_empty_value(value):
    if value is None:
        return True
    if type(value) is int:
        return False
    if len(value) == 0:
        return True
    return False

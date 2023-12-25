

def is_empty_value(value):
    if value is None:
        return True
    if isinstance(value, int):
        return False
    if len(value) == 0:
        return True
    return False

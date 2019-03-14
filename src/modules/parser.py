def parse_string(val):
    return val


def parse_float(val):
    try:
        return float(val)
    except ValueError:
        return None


def parse_int(val):
    try:
        return int(val)
    except ValueError:
        return None


def parse_bool(val):
    if val in ['Yes', 'True', 'true']:
        return True
    elif val in ['No', 'False', 'false']:
        return False
    else:
        return None


FLOAT = parse_float
STRING = parse_string
INT = parse_int
BOOL = parse_bool

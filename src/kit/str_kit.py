
EMPTY = ''


def str_is_none(string):
    return string is None or not isinstance(string, str) or string == EMPTY


def str_is_not_none(string):
    return str_is_none(string) is not True


def str_trim(string):
    if str_is_none(string):
        return EMPTY
    else:
        return str.strip(string)

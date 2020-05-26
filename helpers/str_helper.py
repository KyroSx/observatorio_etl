
def remove_char_from_string(string, char):
    blank = ''
    return string.replace(char, blank)


def switch_char_to_another_char(string, char, another_char):
    string = string.replace(char, another_char)

    return string


def remove_parenthesis(string):
    string = remove_char_from_string(string, '(')
    string = remove_char_from_string(string, ')')

    return string


def switch_comma_to_dot(string):
    sring = string.switch_char_to_another_char(',', '.')

    return string

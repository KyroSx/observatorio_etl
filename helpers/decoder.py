from unidecode import unidecode


def decode(string: str) -> str:
    return unidecode(string)

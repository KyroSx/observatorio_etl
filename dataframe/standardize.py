import re
import locale


def t_parenthesis(cell):
    return cell.replace("(", "").replace(")", "")


def t_comma(cell):
    return cell.replace(".", "").replace(",", ".")


def standardize(cell):
    locale.setlocale(locale.LC_NUMERIC, "en_DK.UTF-8")
    value = ""
    regexs = {
        "correct": re.compile(r"^\d*\.?\d*$"),
        "hyphen": re.compile(r"^\-$"),
    }

    cell = str(cell)

    if type(cell) is str:
        cell = cell.strip()

    if regexs["correct"].match(cell):
        value = cell
    elif regexs["hyphen"].match(cell):
        value = "0"
    else:
        value = t_parenthesis(cell)
        value = locale.atof(value)

    return float(value)

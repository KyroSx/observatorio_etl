import re
import locale
from transform.helpers.str_helper import remove_parenthesis


def standardize_years_values(cell):
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
        value = remove_parenthesis(cell)
        value = locale.atof(value)

    return float(value)


def fix_city_names(city_name: str):
    fixed_city_name = get_correct_city_name(city_name)

    return fixed_city_name


def get_correct_city_name(city_name: str):
    return {
        "Belém de São Francisco": "Belém do São Francisco",
        "Biritiba-Mirim": "Biritiba Mirim",
        "Brasópolis": "Brazópolis",
        "Couto de Magalhães": "Couto Magalhães",
        "Eldorado dos Carajás": "Eldorado do Carajás",
        "Embu": "Embu das Artes",
        "Florínia": "Florínea",
        "Iguaraci": "Iguaracy",
        "Itapagé": "Itapajé",
        "Lagoa do Itaenga": "Lagoa de Itaenga",
        "Moji Mirim": "Mogi Mirim",
        "Muquém de São Francisco": "Muquém do São Francisco",
        "Olho-d'Água do Borges": "Olho d'Água do Borges",
        "Parati": "Paraty",
        "Passa-Vinte": "Passa Vinte",
        "Pingo-d'Água": "Pingo d'Água",
        "Poxoréo": "Poxoréu",
        "Santa Isabel do Pará": "Santa Izabel do Pará",
        "Santana do Livramento": "Sant'Ana do Livramento",
        "Seridó": "Junco do Serido",
        "São Domingos de Pombal": "São Domingos",
        "São Luís do Paraitinga": "São Luíz do Paraitinga",
        "São Valério da Natividade": "São Valério",
        "Trajano de Morais": "Trajano de Moraes"
    }.get(city_name, city_name)

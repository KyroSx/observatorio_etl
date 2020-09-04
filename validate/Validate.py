import pandas
import re
import locale
from dataclasses import dataclass
from models.Fundeb import Fundeb


def remove_char_from_string(string, char):
    blank = ''
    return string.replace(char, blank)


def remove_parenthesis(string):
    string = remove_char_from_string(string, '(')
    string = remove_char_from_string(string, ')')

    return string


@dataclass
class Validate:

    fundeb_obj: Fundeb
    fundeb_validated: pandas.DataFrame = pandas.DataFrame([])

    def start(self):
        self.fundeb_validated = self.fundeb_obj.dataframe

        city_col = self.fundeb_obj.city
        cities_series = self.fundeb_obj.get_all_city_uf_series()

        self.fundeb_validated[city_col] = cities_series.apply(
            self._fix_city_names)

        for year in self.fundeb_obj.years:
            years_series = self.fundeb_obj.get_year_series(year=year)
            self.fundeb_validated[year] = years_series.apply(
                self._standardize_years_values)

    def end(self):
        self.fundeb_obj.dataframe = self.fundeb_validated
        return self.fundeb_obj

    def _standardize_years_values(self, cell):
        locale.setlocale(locale.LC_NUMERIC, "en_DK.UTF-8")
        value = ""
        regexes = {
            "correct": re.compile(r"^\d*\.?\d*$"),
            "hyphen": re.compile(r"^\-$"),
        }

        cell = str(cell)

        if type(cell) is str:
            cell = cell.strip()

        if regexes["correct"].match(cell):
            value = cell
        elif regexes["hyphen"].match(cell):
            value = "0"
        else:
            value = remove_parenthesis(cell)
            value = locale.atof(value)

        return float(value)

    def _fix_city_names(self, city_name: str):
        return self._get_correct_city_name(city_name)

    '''
    def _get_correct_city_name(self, city_name: str):
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
            # "Santa Teresinha": "Santa Terezinha",
            "Santana do Livramento": "Sant'Ana do Livramento",
            "Seridó": "Junco do Seridó",
            "São Domingos de Pombal": "São Domingos",
            "São Luís do Paraitinga": "São Luiz do Paraitinga",
            "São Valério da Natividade": "São Valério",
            "Trajano de Morais": "Trajano de Moraes"
        }.get(city_name, city_name)
    '''

    def _get_correct_city_name(self, city_name: str):
        comaprison = {
            "Belém de São Francisco-PE": "Belém do São Francisco",
            "Biritiba-Mirim-SP": "Biritiba Mirim",
            "Brasópolis-MG": "Brazópolis",
            "Couto de Magalhães-TO": "Couto Magalhães",
            "Eldorado dos Carajás-PA": "Eldorado do Carajás",
            "Embu-SP": "Embu das Artes",
            "Florínia-SP": "Florínea",
            "Iguaraci-PE": "Iguaracy",
            "Itapagé-CE": "Itapajé",
            "Lagoa do Itaenga-PE": "Lagoa de Itaenga",
            "Moji Mirim-SP": "Mogi Mirim",
            "Muquém de São Francisco-BA": "Muquém do São Francisco",
            "Olho-d'Água do Borges-RN": "Olho d'Água do Borges",
            "Parati-RJ": "Paraty",
            "Passa-Vinte-MG": "Passa Vinte",
            "Pingo-d'Água-MG": "Pingo d'Água",
            "Poxoréo-MT": "Poxoréu",
            "Santa Isabel do Pará-PA": "Santa Izabel do Pará",
            # "Santa Teresinha": "Santa Terezinha",
            "Santana do Livramento-RS": "Sant'Ana do Livramento",
            "Seridó-PB": "Junco do Seridó",
            "São Domingos de Pombal-PB": "São Domingos",
            "São Luís do Paraitinga-SP": "São Luiz do Paraitinga",
            "São Valério da Natividade-TO": "São Valério",
            "Trajano de Morais-RJ": "Trajano de Moraes"
        }
        return comaprison.get(city_name, city_name)

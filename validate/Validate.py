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

    def _get_correct_city_name(self, city_name: str) -> str:
        comparison = {
            "Belém de São Francisco-PE": "Belém do São Francisco-PE",
            "Biritiba-Mirim-SP": "Biritiba Mirim-SP",
            "Brasópolis-MG": "Brazópolis-MG",
            "Couto de Magalhães-TO": "Couto Magalhães-TO",
            "Eldorado dos Carajás-PA": "Eldorado do Carajás-PA",
            "Embu-SP": "Embu das Artes-SP",
            "Florínia-SP": "Florínea-SP",
            "Iguaraci-PE": "Iguaracy-PE",
            "Itapagé-CE": "Itapajé-CE",
            "Lagoa do Itaenga-PE": "Lagoa de Itaenga-PE",
            "Moji Mirim-SP": "Mogi Mirim-SP",
            "Muquém de São Francisco-BA": "Muquém do São Francisco-BA",
            "Olho-d'Água do Borges-RN": "Olho d'Água do Borges-RN",
            "Parati-RJ": "Paraty-RJ",
            "Passa-Vinte-MG": "Passa Vinte-MG",
            "Pingo-d'Água-MG": "Pingo d'Água-MG",
            "Poxoréo-MT": "Poxoréu-MT",
            "Santa Isabel do Pará-PA": "Santa Izabel do Pará-PA",
            "Santana do Livramento-RS": "Sant'Ana do Livramento-RS",
            "Seridó-PB": "Junco do Seridó-PB",
            "São Domingos de Pombal-PB": "São Domingos-PB",
            "São Luís do Paraitinga-SP": "São Luiz do Paraitinga-SP",
            "São Valério da Natividade-TO": "São Valério-TO",
            "Trajano de Morais-RJ": "Trajano de Moraes-RJ",
            "Presidente Juscelino-RN": "Serra Caiada-RN",
            "Santa Teresinha-BA": "Santa Terezinha-BA"
        }

        return comparison.get(city_name, city_name)

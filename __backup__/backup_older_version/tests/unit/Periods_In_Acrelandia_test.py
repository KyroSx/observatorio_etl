import unittest
import pandas
from tests.unit.helpers.data_test import DataTest
from src.transform.period import (calculate_period)


class TestSumsInAcrelandiaPeriods(unittest.TestCase):

    def test_get_acrelandia_data(self):
        dt = DataTest()
        data = dt.get_data_input()
        years = [f'{y}' for y in range(2007, 2020)]
        columns = ['Município', 'UF', 'Mês'] + years
        df = pandas.DataFrame(
            data, columns=columns)

        self.assertIsInstance(df, pandas.DataFrame)

        return df

    def test_acrelandia_yearly(self):
        dt = DataTest()
        correct_output = [3773651.1, 5089382.65, 5262367.19,
                          5682387.07, 6687641.83, 6535497.11,
                          6880002.1, 7481952.53, 7602625.99,
                          8385945.55, 8485707.1, 8667882.31,
                          8227686.52]

        period = 'yearly'
        index = 1
        correct_output_values = dt.get_data_output_correct_yearly(
            (correct_output, index, period))

        info = {
            'period': period,
            'correct_output_values': correct_output_values
        }

        self.test_get_periods_generic(info)

    def test_get_periods_generic(self, info={}):
        if not info:
            return

        df_formated = self.test_get_acrelandia_data()
        period, correct_output_values = info.values()

        response = calculate_period(period, df_formated, '')

        self.assertListEqual(response, correct_output_values)

    '''
    yearly 2019: correct_value = [8227686.52] 
    half 2019: correct_value = [4694340.80, 3533345.72]
    quarterly: correct_value = [2474059.81, 2220280.99,
                                2124081.28, 1409264.44]
    bim: correct_value = [1762356.65, 1430109.10,
                         1501875.05, 1456468.76,
                         1319515.64, 757361.32]                    
   '''

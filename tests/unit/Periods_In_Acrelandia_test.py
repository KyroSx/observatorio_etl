import unittest
import pandas
from periods.period import get_sums_list, get_period_object_list


class TestSumsInAcrelandiaPeriods(unittest.TestCase):

    def get_acrelandia_series_2019(self):
        num = [i for i in range(12, 24)]
        datas = [
            861747.15, 900609.50, 711703.16,
            718405.94, 825357.96, 676517.09,
            760446.15, 696022.61, 667612.52,
            651903.12, 757361.32, 0]

        series = pandas.Series(datas, index=num)

        return series

    def get_response_from_sums_list(self, period_value):
        ''' Before each '''
        data = self.get_acrelandia_series_2019()

        response = get_sums_list(period_value, data)

        return response

    def test_yearly_sum_in_acrelandia_2019(self):
        ''' It should return correct sum on yearly '''
        response = self.get_response_from_sums_list(12)
        correct_value = [8227686.52]

        self.assertListEqual(response, correct_value)

        ''' result list should have one value only '''
        size = len(response)
        ANNUAL_SIZE = 1

        self.assertEqual(size, ANNUAL_SIZE)

    def test_half_yearly_sum_in_acrelandia_2019(self):
        ''' It should return correct sum on half-yearly '''
        response = self.get_response_from_sums_list(6)
        correct_value = [4694340.80, 3533345.72]

        self.assertListEqual(response, correct_value)

        ''' result list should have 2 values '''
        size = len(response)
        SEMESTRAL_SIZE = 2

        self.assertEqual(size, SEMESTRAL_SIZE)

    def test_quarterly_sum_in_acrelandia_2019(self):
        ''' it should return 4 correct quarterly values '''
        response = self.get_response_from_sums_list(3)
        correct_value = [2474059.81, 2220280.99,
                         2124081.28, 1409264.44]

        self.assertListEqual(response, correct_value)

        ''' result list should have 4 values '''
        size = len(response)
        TRIMESTRAL_SIZE = 4

        self.assertEqual(size, TRIMESTRAL_SIZE)

    def test_bimonthly_sum_in_acrelandia_2019(self):
        ''' it should return 6 correct bimonthly values '''
        response = self.get_response_from_sums_list(2)

        correct_value = [1762356.65, 1430109.10,
                         1501875.05, 1456468.76,
                         1319515.64, 757361.32]

        self.assertListEqual(response, correct_value)

        ''' result list should have 6 values '''
        size = len(response)
        BIMESTRAL_SIZE = 6

        self.assertEqual(size, BIMESTRAL_SIZE)

    def test_get_period_object_list_in_acrelandia_2019(self):
        ''' This need to be done after refact the actual code '''
        period = "anual"
        city_data = ''
        city_name = 'Acrelândia'
        year = '2019'

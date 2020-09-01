import unittest

from stage.ReferencePeriode import ReferencePeriode


class ReferencePeriodeTest(unittest.TestCase):
    sut: ReferencePeriode

    class Periods:
        BIMONTHLY = 'bimonthly'
        QUARTERLY = 'quarterly'
        HALF_YEARLY = 'half-yearly'
        YEARLY = 'yearly'

    def setUp(self):
        self.sut = ReferencePeriode()

    def test_valid_leap_year(self):
        '''::it should assert true for all valid leap years '''
        years = [
            '1980', '1984', '1988', '1992', '1996', '2000',
            '2004', '2008', '2012', '2016', '2020', '2024',
            '2028', '2032', '2036', '2040', '2044', '2048',
            '2052', '2056', '2060', '2064', '2068', '2072',
            '2076', '2080', '2084', '2088', '2092', '2096',
        ]

        for year in years:
            self.assertTrue(self.sut._is_leap_year(year))

    def test_invalid_leap_year(self):
        '''::it should assert false for all years '''
        years = [
            '1981', '1934', '1985', '1993', '1991', '2007',
            '2003', '2011', '2013', '2017', '2019', '2022',
            '2027', '2031', '2033', '2039', '2023', '2045',
        ]

        for year in years:
            self.assertFalse(self.sut._is_leap_year(year))

    def test_reference_period_strategy_bim(self):
        '''::it should return the correct list for bimonthly '''
        bim_list, _ = self.sut._reference_period_strategy(
            self.Periods.BIMONTHLY)

        self.assertListEqual(bim_list, [1, 3, 5, 7, 9, 11])

    def test_reference_period_strategy_quarterly(self):
        '''::it should return the correct list for quarterly '''
        qr_list, _ = self.sut._reference_period_strategy(
            self.Periods.QUARTERLY)

        self.assertListEqual(qr_list, [1, 4, 7, 10])

    def test_reference_period_strategy_half_yearly(self):
        '''::it should return the correct list for half-yearly '''
        hy_list, _ = self.sut._reference_period_strategy(
            self.Periods.HALF_YEARLY)

        self.assertListEqual(hy_list, [1, 7])

    def test_reference_period_strategy_yearly(self):
        '''::it should return the correct list for yearly '''
        y_list, _ = self.sut._reference_period_strategy(
            self.Periods.YEARLY)

        self.assertListEqual(y_list, [1])

    def test_get_reference_period_bim(self):
        '''::it should return the (in, until) correctly '''
        rp = self.sut.get_reference_period(
            period_type=self.Periods.BIMONTHLY,
            index=1, year=2007)

        self.assertEqual(rp, ('2007-01-01', '2007-02-28'))

     def test_get_reference_period_yearlY(self):
        '''::it should return the (in, until) correctly '''
        rp = self.sut.get_reference_period(
            period_type=self.Periods.YEARLY,
            index=1, year=2007)

        self.assertEqual(rp, ('2007-01-01', '2007-12-31'))

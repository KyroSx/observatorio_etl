import unittest

from stage.ReferencePeriode import ReferencePeriode


class ReferencePeriodeTest(unittest.TestCase):
    sut: ReferencePeriode

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

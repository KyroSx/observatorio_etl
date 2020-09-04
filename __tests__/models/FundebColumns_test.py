import unittest

from models.FundebColumns import FundebColumns


class TestFundebColumns(unittest.TestCase):

    def test_all(self):
        self.assertListEqual(
            FundebColumns.ALL_COLS,
            ['Município', 'UF', 'Município - UF',
             'Mês', '2007', '2008', '2009', '2010', '2011',
             '2012', '2013', '2014', '2015', '2016', '2017',
             '2018', '2019'])

    def test_reduced_cols(self):
        self.assertListEqual(
            FundebColumns.REDUCED_COLS,
            ['Município - UF', 'Mês', '2007',
             '2008', '2009', '2010', '2011',
             '2012', '2013', '2014', '2015',
             '2016', '2017', '2018', '2019'])

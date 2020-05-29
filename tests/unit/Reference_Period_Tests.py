import unittest
from periods.reference_period import (get_reference_period,
                  transform_string_to_date, is_leap_year)
import datetime


class Test(unittest.TestCase):

    def test_is_leap(self):
        """ Should identify if a year is leap 🎉 """
        years = [
            1004, 1008, 1012, 1016, 1020, 1024, 1028,
            1032, 1036, 1040, 1044, 1048, 1052, 1056,
            1060, 1064, 1068, 1072, 1076, 1080, 2000,
            2004, 2008, 2012, 2016, 2020, 2024, ]
        years_result = []

        for year in years:
            years_result.append(is_leap_year(year))

        for resultant in years_result:
            self.assertTrue(resultant)

    def test_reference_period_bimonthly(self):
        """ Should return correct ref_period to all bimonthly in a year 2️⃣ """
        in_correct_list = [
            '2016-01-01', '2016-03-01', '2016-05-01',
            '2016-07-01', '2016-09-01', '2016-11-01', ]

        unil_correct_list = [
            '2016-02-29', '2016-04-30', '2016-06-30',
            '2016-08-31', '2016-10-31', '2016-12-31', ]

        infos = {
            "BIM": "bimonthly",
            "YEAR": 2016,
            "in_correct_list": in_correct_list,
            "until_correct_list": unil_correct_list,
            "ranged": range(1, 7)
        }

        self.test_reference_period(infos)

    def test_reference_period_quarterly(self):
        """ Should return correct ref_period to all quarterly in a year 3️⃣ """
        in_correct_list = [
            '2016-01-01', '2016-04-01',
            '2016-07-01', '2016-10-01', ]
        unil_correct_list = [
            '2016-03-31', '2016-06-30',
            '2016-09-30', '2016-12-31', ]

        infos = {
            "BIM": "quarterly",
            "YEAR": 2016,
            "in_correct_list": in_correct_list,
            "until_correct_list": unil_correct_list,
            "ranged": range(1, 5)
        }

        self.test_reference_period(infos)

    def test_reference_period_half_yearly(self):
        """ Should return correct ref_period to all semesters in a year 6️⃣ """
        in_correct_list = ['2016-01-01', '2016-07-01']
        unil_correct_list = ['2016-06-30', '2016-12-31']

        infos = {
            "BIM": "half-yearly",
            "YEAR": 2016,
            "in_correct_list": in_correct_list,
            "until_correct_list": unil_correct_list,
            "ranged": range(1, 3)
        }

        self.test_reference_period(infos)

    def test_reference_period_yearly(self):
        """ 1️⃣2️⃣"""
        in_correct_list = ['2016-01-01', ]
        unil_correct_list = ['2016-12-31', ]

        infos = {
            "BIM": "yearly",
            "YEAR": 2016,
            "in_correct_list": in_correct_list,
            "until_correct_list": unil_correct_list,
            "ranged": range(1, 2)
        }

        self.test_reference_period(infos)

    def test_reference_period(self, infos={}):
        """ Generic test to all others periods 🎭 """
        if not infos:
            return

        PERIOD, YEAR, in_correct_list, unil_correct_list, ranged = \
            infos.values()

        in_list = []
        until_list = []
        in_correct_formated = []
        until_correct_formated = []

        for index in ranged:
            in_b, until_b = get_reference_period(PERIOD, YEAR, index)
            in_list.append(in_b)
            until_list.append(until_b)

            in_f = transform_string_to_date(in_correct_list[index-1])
            in_correct_formated.append(in_f)

            until_f = transform_string_to_date(unil_correct_list[index-1])
            until_correct_formated.append(until_f)

        self.assertListEqual(in_list, in_correct_formated)
        self.assertListEqual(until_list, until_correct_formated)

    def test_transform_string_to_date(self):
        """ Should return correct date from string 📅 """
        iny = transform_string_to_date('2016-01-01')
        untily = transform_string_to_date('2016-02-28')

        inc = datetime.date(year=2016, month=1, day=1)

        self.assertEqual(iny, inc)
        self.assertIsInstance(iny, datetime.date)
        self.assertIsInstance(untily, datetime.date)

import unittest
from dataframe.standardize import standardize


class TestStandardizeInAcrelandia(unittest.TestCase):

    def test_standardize_acrelandia_2019(self):
        result = []
        unformated_data = ['861.747,15', '900.609,50', '711.703,16',
                           '718.405,94', '825.357,96', '676.517,09',
                           '760.446,15', '696.022,61', '667.612,52',
                           '651.903,12', '757.361,32', '-', '(1.92,5)']

        for undata in unformated_data:
            data = standardize(undata)
            result.append(data)

        formated_data = [861747.15, 900609.50, 711703.16,
                         718405.94, 825357.96, 676517.09,
                         760446.15, 696022.61, 667612.52,
                         651903.12, 757361.32, 0, 192.5]

        self.assertListEqual(result, formated_data)

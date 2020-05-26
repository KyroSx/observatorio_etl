import unittest
from database.connection import create_database_object
from helpers.str_helper import remove_parenthesis, remove_char_from_string
from data.Data_Object import create_data_object


class TestDataBase(unittest.TestCase):
    def test_get_city_id_by_name(self):
        city_name = 'Acrelândia'
        city_id_list = ['1200013']

        database = create_database_object()
        city_id_returned = database.get_city_id_by_name(city_name)

        city_id_returned = map(lambda x: remove_parenthesis(str(x)),
                               city_id_returned)
        city_id_returned = map(lambda x: remove_char_from_string(x, ','),
                               city_id_returned)

        city_id_returned_list = list(city_id_returned)

        for index in range(len(city_id_returned_list)):
            self.assertEqual(city_id_returned_list[index],
                             city_id_list[index])

    def test_insert_data_object(self):
        db = create_data_object(city_name='Acrelândia',
                                value=3773651.1, year=2007,
                                period='yearly', index=1)
        pass

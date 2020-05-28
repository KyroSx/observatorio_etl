import unittest
from database.connection import create_database_object
from helpers.str_helper import remove_parenthesis, remove_char_from_string
from data.Data_Object import create_data_object, Data_Object


class TestDataBase(unittest.TestCase):
    def test_get_city_id_by_name(self):
        city_name = ['Acrelândia', 'Guarapuava', 'Prudentópolis']
        city_id_list = ['1200013', '4109401', '4120606']
        city_id_returned_list = []

        database = create_database_object()
        for index in range(len(city_name)):
            city_id_returned = database.get_city_id_by_name(city_name[index])
            city_id_returned_list.append(city_id_returned[0])

            city_id_returned_list = list(city_id_returned_list)

        self.assertListEqual(city_id_returned_list, city_id_list)

    def test_insert_data_object(self):
        data_dict = {
            "period": 'yearly',
            "value": 3773651.1,
            "year": '2007',
            "city_name": 'Acrelândia',
            "index": 1
        }
        db = create_data_object(data_dict)
        self.assertIsInstance(db, Data_Object)

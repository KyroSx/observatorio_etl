import unittest
from datetime import datetime

from src.load.database.connection import create_database_object
from src.load.reference_period import transform_string_to_date

from src.transform.helpers.str_helper import (
    remove_parenthesis, remove_char_from_string)
from src.transform.models.Data_Object import (
    create_data_object, Data_Object)
from src.load.database.querys.query import (
    create_query_object)


class TestDataBase(unittest.TestCase):

    database = ''

    def setUp(self):
        ''' Before each '''
        database = create_database_object()

        query_object = create_query_object(database)

        self.database = query_object

    def test_get_granularity_id_from_period(self):

        granularitys = [
            'bimonthly', 'quarterly',
            'half-yearly', 'yearly']

        granularitys_ids = ['1', '2', '3', '4']

        info = {
            'input_list': granularitys,
            'correct_list': granularitys_ids,
            'output_number': 0
        }

        self.test_generic_query_db(
            function=self.database.get_granularity_id_from_period,
            info=info)

    def test_get_information_and_data_type_id(self):

        information_nick_name = ['FUNDEB']
        information_id = ['1']

        data_type = ['float']
        data_type_id = ['1']

        info = {
            'input_list': information_nick_name,
            'correct_list': information_id,
            'output_number': 0
        }

        self.test_generic_query_db(
            function=self.database.get_information_id_from_nick_name,
            info=info)

        info = {
            'input_list': data_type,
            'correct_list': data_type_id,
            'output_number': 0
        }

        self.test_generic_query_db(
            function=self.database.get_data_type_id,
            info=info)

    def test_get_city_id_by_name(self):
        ''' Test if the data:name == locations:id '''

        city_name = ['Acrelândia', 'Guarapuava', 'Prudentópolis']
        city_id_list = ['1200013', '4109401', '4120606']

        info = {
            'input_list': city_name,
            'correct_list': city_id_list,
            'output_number': 0
        }
        self.test_generic_query_db(function=self.database.get_city_id_by_name,
                                   info=info)

    @unittest.expectedFailure
    def test_get_reference_period_id_from_period(self):
        datetime_format = '%Y-%m-%d'
        def parse(string): return datetime.strptime(
            string, datetime_format).date()

        in_until_list = [
            {"in": parse('2007-01-01'), "until": parse('2007-02-28')}
        ]

        correct_reference_id = [None]

        info = {
            'input_list': in_until_list,
            'correct_list': correct_reference_id,
            'output_number': 0
        }

        self.test_generic_query_db(
            info=info,
            function=self.database.get_reference_period_id_from_periods_dates)

    def test_generic_query_db(self, info={}, function=None):
        """ Template test for database querys 🎲 """
        if not info and not function:
            return

        input_list, correct_list, output_number = info.values()
        output_list = []

        for input_item in input_list:
            output_item = function(input_item)
            if output_item:
                output_list.append(output_item[output_number])

        self.assertListEqual(output_list, correct_list)

    def test_insert_data_object(self):
        ''' Test if a data object is inserted on database '''
        data_dict = {
            "period": 'yearly',
            "value": 3773651.1,
            "year": '2007',
            "city_name": 'Acrelândia',
            "index": 1
        }
        db = create_data_object(data_dict)
        self.assertIsInstance(db, Data_Object)

from transform.period import calculate_period
from load.database.connection import create_database_object
from load.database.querys.query import create_query_object
from transform.helpers.str_helper import remove_char_from_string
from load.reference_period import get_reference_period
from transform.models.Data_Object import Data_Object
from pandas import Series

from unidecode import unidecode


def get_reference_periode_from_object(data_periode: Data_Object):

    data: tuple = data_periode.get_all_values_tuple()

    period, _value, year, _city_name, _uf, index = data

    period_r = get_reference_period(period, year, index)  # 1.38

    """ print(city_name, index, period, year, value)
    print(period_r[0], period_r[1])
    print(locations[unidecode(city_name)]) """

    data_periode.reference_periode = period_r

    return data_periode


def get_all_reference_periodes_from_series(data_periode_object_serie: Series):
    return data_periode_object_serie.apply(
        get_reference_periode_from_object)


def apply_locations(data_periode_object_serie: Series):

    d = create_database_object()
    d.start_connection()
    c = d.cnx.cursor()

    query = 'SELECT idIBGE, idIBGE_MemberOf, name, type, nickName  FROM Locations'

    c.execute(query)

    locations = {f'{unidecode(name)}': (idIBGE, nickName, idIBGE_MemberOf, typed)
                 for idIBGE, idIBGE_MemberOf, name, typed, nickName in c}

    d.close_connection()

    def gl(data_object): return data_object.location_city_name, locations[unidecode(
        data_object.location_city_name)]

    print(data_periode_object_serie.apply(gl))
    print(locations['Parana'])

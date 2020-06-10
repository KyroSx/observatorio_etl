from src.transform.period import calculate_period


def create_data_object_dict_list(city_name: str,
                                 city_uf: str,
                                 list_of_periodes_sum: list):
    list_data_dicts = []
    for list_periode in list_of_periodes_sum:
        for periode_sum in list_periode:
            year, index, periode, value = periode_sum

            data_dict = {
                'city_name': city_name,
                'UF': city_uf,
                'year': year,
                'index': index,
                'periode': periode,
                'value': value
            }

            list_data_dicts.append(data_dict)
    return list_data_dicts


def calculate_all_periods_sums(city_grouped, city_name: str,
                               city_uf: str):
    periods = ['bimonthly', 'quarterly',
               'half-yearly', 'yearly']
    list_of_periodes_sum = []
    list_data_dicts = []
    for period in periods:
        list_of_periodes_sum = calculate_period(period, city_grouped)
        list_data_dicts += create_data_object_dict_list(
            city_name, city_uf, list_of_periodes_sum)

    return list_data_dicts

from data.Data_Object import create_data_object


def period_options(period) -> int:
    periods = {
        "bimestral": 2,
        "trimestral": 3,
        "semestral": 6,
        "anual": 12
    }
    return periods.get(period, "Not a valid period")


def get_sums_list(period_value, city_data_year) -> list:
    city_period_sum_list = []

    start_interval = 0
    end_interval = period_value

    size = int(len(city_data_year)/period_value)

    for i in range(size):
        city_period_sliced = city_data_year[start_interval:end_interval]
        city_period_sum = city_period_sliced.sum()

        city_period_sum_rounded = round(city_period_sum, 2)
        city_period_sum_list.append(city_period_sum_rounded)

        start_interval = end_interval
        end_interval += period_value

    return city_period_sum_list


def get_period_object_list(period, city_data, city_name, year) -> list:
    period_value = period_options(period)

    city_data_year = city_data[year]

    city_period_sum_list = get_sums_list(period_value, city_data_year)
    city_period_object_list = []

    for index, value in enumerate(city_period_sum_list):
        data_o = create_data_object(
            period, value,
            year, city_name,
            index + 1
        )
        city_period_object_list.append(data_o)

    return city_period_object_list

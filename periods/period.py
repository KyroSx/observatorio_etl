
def period_options(period) -> int:
    periods = {
        "bimestral": 2,
        "trimestral": 3,
        "semestral": 6,
        "anual": 12
    }

    return periods.get(period, "Not a valid period")

def get_period(period, city_data, city_name, year):
    period_value = period_options(period)

    start_interval = 0
    end_interval = period_value

    city_data_year = city_data[year]

    size = int(len(city_data_year)/period_value)
    print(f'size is {size}')
    for c in range(size):
        city_period_sliced = city_data_year[start_interval:end_interval]
        city_period_sum = city_period_sliced.sum()

        start_interval = end_interval
        end_interval += period_value

        print(f"{city_name}#{year}:")
        print(f"sum is: {city_period_sum}")


def period_constants(period) -> int:
    periodes = {
        "bimonthly": 2,
        "quarterly": 3,
        "half-yearly": 6,
        "yearly": 12
    }
    period_value = periodes.get(period, "Not a valid period")

    return period_value


def period_options(period):
    period_value = period_constants(period)
    total_months = 12
    final_interval = (total_months / period_value) + (1)

    inverval = range(1, int(final_interval))
    def start_interval(i): return (i*period_value)-(period_value-1)
    def end_interval(i): return (i*period_value)

    return (inverval, start_interval, end_interval)


def calculate_period(period, city_grouped):
    inverval, start_inteval, end_interval = \
        period_options(period)

    years = [f"{year}" for year in range(2007, 2020)]

    result_list = []
    for index in inverval:
        sliced = city_grouped[
            (city_grouped['Mês'] >= (start_inteval(index))) &
            (city_grouped['Mês'] <= (end_interval(index)))
        ].sum()

        result_years_list = []
        for year in years:
            value = round(sliced[year], 2)
            result = (year, index, period, value)
            result_years_list.append(result)

        result_list.append(result_years_list)

    return result_list


def period_options(period) -> int:
    periods = {
        "bimestral": 2,
        "trimestral": 3,
        "semestral": 6,
        "anual": 12
    }

    return periods.get(period, "Not a valid period")

def get_period(period, fundeb, year):
    period_value = period_options(period)
    limit = period_value - 1
    year_len = fundeb[year].size
    scope = range(0, year_len, period_value -1)

    for i in scope:
        received = fundeb[year].loc[i:(i+limit)]
        sums = received.sum()
        print(f'{period}#{i} is ${sums}')

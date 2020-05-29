from datetime import datetime


def transform_string_to_date(string):
    """ Transform a string in datetime.date """
    datetime_format = '%Y-%m-%d'
    parsed = datetime.strptime(string, datetime_format)
    return parsed.date()


def get_day_and_month(start_month_list, index, ratio):
    """ Return day and month variables to calculate period """
    delta = index*ratio
    end_day = get_end_day(delta)
    start_month = start_month_list[index-1]
    end_month = delta

    return end_day, start_month, end_month


def is_leap_year(year):
    """ Identify if a year is leap """
    year = int(year)

    if year % 4 == 0:
        if year % 100 != 0:
            return True
    if year % 400 == 0:
        return True

    return False


def referece_period_strateggy(period_type: str):
    """ Design pattern to return calculations variables """
    periods = {
        'bimonthly': ([x for x in range(1, 12) if x % 2 == 1], 2),
        'quarterly': ([x for x in range(1, 12, 3)], 3),
        'half-yearly': ([x for x in range(1, 12, 6)], 6),
        'yearly': ([x for x in range(1, 12, 12)], 12)
    }
    return periods.get(period_type)


def get_reference_period(period_type, year, index) -> tuple:
    start_day = 1

    start_month_list, ratio = referece_period_strateggy(period_type)

    end_day, start_month, end_month = get_day_and_month(
        start_month_list, index, ratio)

    is_leap = is_leap_year(year)
    if is_leap and end_month == 2:
        end_day += 1

    in_date = transform_string_to_date(f'{year}-{start_month}-{start_day}')
    until_date = transform_string_to_date(f'{year}-{end_month}-{end_day}')

    return in_date, until_date


def get_end_day(month):
    ''' Return the last day of a month '''
    return {
        2: 28,
        3: 31,
        4: 30,
        6: 30,
        8: 31,
        9: 30,
        10: 31,
        12: 31
    }.get(month)

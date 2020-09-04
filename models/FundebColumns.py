class FundebColumns:
    UF = 'UF'
    CITY_NAME = 'Município'
    CITY_UF = 'Município - UF'
    MONTH = 'Mês'
    YEARS = [str(year) for year in range(2007, 2020)]

    ALL_COLS = [
        CITY_NAME,
        UF,
        CITY_UF,
        MONTH
    ] + YEARS

    REDUCED_COLS = [
        CITY_UF,
        MONTH
    ] + YEARS

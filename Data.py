class Data_Object:
    def __init__(self,
                 period_type, value,
                 location_year, location_city_name
                 ):
        self.period_type = period_type
        self.value = value
        self.location_year = location_year
        self.location_city_name = location_city_name

    def __str__(self):
        a = f"{self.location_city_name}#{self.location_year}:\n"
        b = f"{self.period_type} -> ${self.value}"
        return a + b

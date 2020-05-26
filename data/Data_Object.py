
class Data_Object:
    def __init__(self,
                 period_type, value, index,
                 location_year, location_city_name):
        self.period_type = period_type
        self.value = value
        self.location_year = location_year
        self.location_city_name = location_city_name
        self.index = index

    def __str__(self):
        a = f"{self.location_city_name}#{self.location_year}:\n"
        b = f"{self.index}º {self.period_type} -> ${self.value}"
        return a + b


def create_data_object(period, value,
                       year, city_name,
                       index):
    data_o = Data_Object(period, value,
                         year, city_name, index)
    return data_o

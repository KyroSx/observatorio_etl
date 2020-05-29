from dataclasses import dataclass


@dataclass
class Data:
    id: int
    data: float
    idInformation: int
    idInformationDataType: int
    idPeriod: int
    idLocation: int
    idGranularity: int


@dataclass
class Data_Object:
    """ Representation of Data Table on DW """
    granularity: str
    value: float
    location_year: str
    location_city_name: str
    index: int

    def __str__(self):
        string = f''
        string = f"{self.location_city_name}#{self.location_year}:\n"
        string += f"{self.index}º {self.granularity} -> ${self.value}"
        return string


def create_data_object(data_dict):
    period, value, year, city_name, index = data_dict.values()
    data_o = Data_Object(period, value,
                         year, city_name, index)
    return data_o

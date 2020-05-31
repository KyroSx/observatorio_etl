from dataclasses import dataclass


@dataclass
class Data:
    """ Representation of Data Table on DW """
    data: float
    idInformation: int
    idInformationDataType: int
    idPeriode: int
    idLocation: int
    idGranularity: int

    def __str__(self):
        string = f'({self.data}, {self.idInformation}, {self.idPeriode}, '
        string += f'{self.idLocation}, {self.idGranularity})'
        return string


@dataclass
class Data_Object:
    """ Representation Periode Sum """
    granularity: str
    value: float
    location_year: str
    location_city_name: str
    index: int

    def __str__(self):
        string = f"{self.location_city_name}#{self.location_year}:\n"
        string += f"{self.index}º {self.granularity} -> ${self.value}"

        return string


def create_data_object(data_dict: {}):
    city_name, year, index, period, value = data_dict.values()
    data_o = Data_Object(granularity=period, value=value,
                         location_year=year, location_city_name=city_name,
                         index=index)
    return data_o


def create_object_list(dict_list):
    data_object_list = []
    for data_dict in dict_list:
        data = create_data_object(data_dict)
        data_object_list.append(data)

    return data_object_list

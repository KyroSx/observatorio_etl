from extract.Extract import Extract
from validate.Validate import Validate
from transform.Transform import Transform
from stage.Stage import Stage
from load.database.Database import Database

from models.Fundeb import Fundeb

# Extract Layer
extract = Extract(number_of_rows=120)
extract.start()

fundeb_dataframe = extract.end()
fundeb_obj = Fundeb(dataframe=fundeb_dataframe)

# Validation Layer
validate = Validate(fundeb_obj=fundeb_obj)
validate.start()

fundeb_obj_validated = validate.end()

# Transform layer
transform = Transform(fundeb_obj_validated, '')
transform.start()

periode_summed_series = transform.end()

# Stage layer
stage = Stage(periode_summed_series=periode_summed_series)
stage.start()
periode_summed_series = stage.end()


# Load layer
db = Database()
db.start_connection()

cur = db.connection.cursor()

get_all_locations_query = 'SELECT idIBGE, idIBGE_MemberOf, name, type, nickName FROM Locations WHERE name=\'Cascavel\' and `type`=\'Município\''

cur.execute(get_all_locations_query)

locations_dict = {
    f'{name}-{idIBGE}': (idIBGE, nickName, idIBGE_MemberOf, typed)
    for idIBGE, idIBGE_MemberOf, name, typed, nickName in cur
}

cur.close()

db.close_connection()

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

# Load layer
db = Database()
db.start_connection()

cursor = db.connection.cursor()

cursor.execute('SELECT * FROM Information')

for r in cursor:
    print(r)

db.close_connection()

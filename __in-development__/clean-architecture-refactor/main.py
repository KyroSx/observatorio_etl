from extract.Extract import Extract
from validate.Validate import Validate
from transform.Transform import Transform
from models.Fundeb import Fundeb

# Extract Layer
extract = Extract()
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

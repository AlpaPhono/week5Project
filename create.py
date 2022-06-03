from application import db

# Code below deletes all exsisting tables and creates the ones defined in the Models 
#(this will probably be changed becasue we dont want to delete existing data in database)
db.drop_all()
db.create_all()
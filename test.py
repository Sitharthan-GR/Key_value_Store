from KeyValue import DataBase
# creating database in Default location

d=DataBase()


# adding values to the  database
d.create("wayne","gotham",5)
d.create("flash","centralcity")
d.create("kent","smallville",1000)
d.create("eren","rose")

#reading values from database

d.Read("wayne")
d.Read("flash")

#Dereneleting value from database

d.Delete("wayne")
d.Delete("eren")
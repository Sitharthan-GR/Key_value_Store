Package name=KeyValue

Info:
    It is used to perform Simple CRD operation in file based key value datastore

FUNCTIONS:

1)DataBase(datastore_location=*opt,datastore_name=*opt)

It is used to instantiate the class and to allocate path to the data store

2)create(key,value,time2live=*opt)

It will add the corresponding key and value to datastore and it will also stores the time2live(which is in seconds)

3) Read(Key)

It will return the corresponding value to the Key and return error if the key expires

4)Delete(Key)

It will delete the key and its value and returns error if the key expires

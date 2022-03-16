#!/usr/bin/python

## import libraries
import pymongo
from pymongo import MongoClient
## set the db connections and select the appropriate collection
client = MongoClient ('localhost',27017)
db=client["miramar"]
mycol = db["SCANNER11"]
## run the iteration to extract the info
lista_devices=[]
for i in list(mycol.find({})):
    lista_devices.append(i['devices'])
## print the results to standard output
print('--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--')
print('list of unique devices in database: ')
print(list(set(lista_devices)))
print('-----------------------------------------------')
print('number of devices in database: ' + str(len(lista_devices)))
print('number of unique devices in database: ' + str(len(set(lista_devices))))
print('--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--')

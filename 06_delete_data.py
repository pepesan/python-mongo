# -*- coding: utf-8 -*-
from pymongo import MongoClient
#include pprint for readabillity of the
from pprint import pprint

#change the MongoClient connection string to your MongoDB database instance
client = MongoClient(port=27017)
db=client.business
result = db.restaurants.delete_many({"category": "Bar Food"})
pprint(result)
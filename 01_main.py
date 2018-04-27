## recuerda instalar pymongo
# python -m pip install pymongo

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
#client = MongoClient(<<MONGODB URL>>)
client = MongoClient("mongodb://localhost/test")
db=client.business
# Issue the serverStatus command and print the results
serverStatusResult=db.command("serverStatus")
pprint(serverStatusResult)
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
#client = MongoClient(<<MONGODB URL>>)
client = MongoClient("mongodb://localhost/test")
db=client.business

fivestar = db.reviews.find_one({'rating': 5})
print(fivestar)

fivestarcount = db.reviews.find({'rating': 5}).count()
print(fivestarcount)
import pymongo
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
print("Número de sitios con 5 estrellas",fivestarcount)

result = db.reviews.find({'rating': 5,'cuisine':"Pizza"}).count()
print("Número de sitios con 5 estrellas de pizza",result)

result = db.reviews.find({'rating': 5,'cuisine':"Pizza"})\
    .limit(10).skip(10)
print("Resultados de la segunda pagina de 10 elementos")
for item in result:
    print(item)

result = db.reviews.find({'rating': 5,'cuisine':"Pizza"})\
    .limit(10).skip(10).sort("name")
print("resultados de ordenación por nombre ascendente")
for item in result:
    print(item)

result = db.reviews.find({'rating': 5,'cuisine':"Pizza"})\
    .limit(10).skip(10).sort("name",pymongo.DESCENDING)
print("Resultados de ordenación descendente")
for item in result:
    print(item)
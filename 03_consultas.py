# -*- coding: utf-8 -*-
from bson.objectid import ObjectId
import pymongo
from pymongo import MongoClient, ReturnDocument
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
#client = MongoClient(<<MONGODB URL>>)
client = MongoClient("mongodb://localhost:27017/business")
#Conectamos a la BBDD
db=client.business
#conectamos a la coleccion reviews
reviews = db.reviews

fivestar = reviews.find_one({'rating': 5})
print(fivestar)

resultado=reviews.insert_one({
    'rating':2,
    'name': "Vips",
    'cuisine':"Italian, o eso dicen",
    'likes':0
})
print(resultado)
print(resultado.inserted_id)

objeto=reviews.find_one(
    {'_id': ObjectId(resultado.inserted_id)})
print("Objeto encontrado por ID:",objeto)

objeto=reviews.find_one_and_update(
    {'_id': ObjectId(resultado.inserted_id)},
    {'$inc': {'likes': 1}, '$set': {'visited': True}},
    return_document=ReturnDocument.AFTER)
print(objeto)

resultado=reviews.find_one_and_delete(
    {'_id': ObjectId(resultado.inserted_id)})
print("Resultado del borrado:",resultado)

fivestarcount = reviews.find({'rating': 5}).count()
print("Numero de sitios con 5 estrellas",fivestarcount)

result = reviews.find({'rating': 5, 'cuisine': "Pizza"}).count()
print("Numero de sitios con 5 estrellas de pizza",result)

result = reviews.find({'rating': 5, 'cuisine': "Pizza"})\
    .limit(10).skip(10)
print("Resultados de la segunda pagina de 10 elementos")
for item in result:
    print(item)

result = reviews.find({'rating': 5, 'cuisine': "Pizza"})\
    .limit(10).skip(10).sort("name")
print("resultados de ordenación por nombre ascendente")
for item in result:
    print(item)

result = reviews.find({'rating': 5, 'cuisine': "Pizza"})\
    .limit(10).skip(10).sort("name",pymongo.DESCENDING)
print("Resultados de ordenación descendente")
for item in result:
    print(item)
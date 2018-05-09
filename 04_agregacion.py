# -*- coding: utf-8 -*-
from pymongo import MongoClient
import pprint
from bson.son import SON
# Connect to the MongoDB, change the connection string per your MongoDB environment
client = MongoClient(port=27017)
# Set the db object to point to the business database
db=client.business
# Showcasing the count() method of find, count the total number of 5 ratings
print('The number of 5 star reviews:')
fivestarcount = db.reviews.find({'rating': 5}).count()
print(fivestarcount)
# Not let's use the aggregation framework to sum the occurrence of each rating across the entire data set
print('\nThe sum of each rating occurance across all data grouped by rating ')
stargroup=db.reviews.aggregate(
# The Aggregation Pipeline is defined as an array of different operations
[
# The first stage in this pipe is to group data
{ '$group':
    { '_id': "$rating",
     "count" :
                 { '$sum' :1 }
    }
},
# The second stage in this pipe is to sort the data
{"$sort":  { "_id":1}
}
# Close the array with the ] tag
] )
# Print the result
for group in stargroup:
    print(group)


result = db.things.insert_many([{"x": 1, "tags": ["dog", "cat"]},
                                 {"x": 2, "tags": ["cat"]},
                                 {"x": 2, "tags": ["mouse", "cat", "dog"]},
                                {"x": 3, "tags": []}])
print(result.inserted_ids)



pipeline = [
     {"$unwind": "$tags"},
     {"$group": {"_id": "$tags", "count": {"$sum": 1}}},
     {"$sort": SON([("count", -1), ("_id", -1)])}
 ]

pprint.pprint(list(db.things.aggregate(pipeline)))


result = db.things.insert_many([{"x": 1, "total":40, "lines": [{"total":20}, {"total":20}]},
                                 {"x": 2, "total":20, "lines": [{"total":10}, {"total":10}]},
                                 {"x": 2, "total":50,"lines": [{"total":20}, {"total":20},{"total":10}]},
                                {"x": 3, "total":0,"lines": []}])
print(result.inserted_ids)



pipeline = [
    {"$group": {"_id": "$x", "media": {"$avg": "$total"}}}
 ]

pprint.pprint(list(db.things.aggregate(pipeline)))
pipeline = [
    {"$group": {"_id": "$x", "total": {"$sum": "$total"}}}
 ]

pprint.pprint(list(db.things.aggregate(pipeline)))
# -*- coding: utf-8 -*-

from pymongo import MongoClient
import pprint
from bson.code import Code
client = MongoClient("mongodb://localhost:27017/business")
db=client.business



mapper = Code("""
               function () {
                 this.tags.forEach(function(z) {
                   emit(z, 1);
                 });
               }
               """)

reducer = Code("""
                function (key, values) {
                  var total = 0;
                  for (var i = 0; i < values.length; i++) {
                    total += values[i];
                  }
                  return total;
                }
                """)
result = db.things.map_reduce(mapper, reducer, "myresults")
for doc in result.find():
   pprint.pprint(doc)


results = db.things.map_reduce(mapper, reducer, "myresults", query={"x": {"$lt": 2}})
for doc in results.find():
    pprint.pprint(doc)


from bson.son import SON
pprint.pprint(
     db.things.map_reduce(
         mapper,
         reducer,
         out=SON([("replace", "results"), ("db", "outdb")]),
         full_response=True))
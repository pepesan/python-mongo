# -*- coding: utf-8 -*-
## recuerda instalar pymongo
# python -m pip install pymongo
import pandas as pd

from pymongo import MongoClient

client = MongoClient("mongodb://localhost/test")
db = client.test


df = pd.read_csv('files/1500000 Sales Records.csv')

#print(df.head())
print(df.shape)
# ordenar por columna
df = df.sort_values(by=['Order ID'])
columns = ['Region', 'Country', 'Item Type', 'Sales Channel', 'Order Priority',
       'Order Date', 'Order ID', 'Ship Date', 'Units Sold', 'Unit Price',
       'Unit Cost', 'Total Revenue', 'Total Cost', 'Total Profit']

print(len(df['Order ID'].unique()))
order_id = None
for index, item in df.iterrows():
    #print(item)
    #print(item['Region'])
    #print(item['Order ID'])
    if order_id == None:
        order_id = item['Order ID']
    else:
        if order_id == item['Order ID']:
            print("coincidencia: " + order_id)
    object = {}
    for col in columns:
        object[col] = item[col]
    #print(object)
    #result = db.sales.insert_one(object)
    if index % 10000 == 0:
        print("Indice: "+ str(index))
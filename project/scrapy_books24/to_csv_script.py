import pandas as pd
import pymongo
import csv


client = pymongo.MongoClient('localhost', 27017)
db = client['books24']

series_collection = db['books24']

coll_list = series_collection.find({})

# преобразование базы данных в csv файл для дальнейшей обработки
with open('books24.csv', 'w', encoding='utf-8', newline='') as csvfile:
    fieldnames = list(coll_list[0].keys())
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(coll_list)

df = pd.read_csv('books24.csv')
print(df.head(3))

import pymongo

# создание клиента
client = pymongo.MongoClient('localhost', 27017)

# подключение к базе
db = client['books24']

# функция для поиска с доп параметром один/все в коллекции
series_collection = db['books24']

def find_books(collection, elements, multiple=False):
    """ Function to retrieve single or multiple documents from a provided
    Collection using a dictionary containing a document's elements.
    """
    if multiple:
        results = collection.find(elements)
        return [r for r in results]
    else:
        return collection.find_one(elements)
    
# результат пишется в словарь с параметром True - выводим все значения , соотв. условиям поиска
result = find_books(series_collection, {"genre": "Зарубежная сентиментальная проза"}, True)

# построчный вывод результатов поиска
print(*result, sep='\n')
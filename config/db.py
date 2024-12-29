from pymongo import MongoClient

client = MongoClient(
    'mongodb+srv://raman9514:admin@cluster0.5lkypkz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

collection = client.urlshorter.URLCollection

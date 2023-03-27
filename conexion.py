import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Parcial-1"]
collections = db["peliculas"]


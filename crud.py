from conexion import collections
import json


def read_peliculas(id=None):
    if id is not None:
        query = {"_id": id}
        document = collections.find_one(query)
        print(document)
    else:
        documents = collections.find()
        for document in documents:
            print(document)


def read_peliculas(Titulo=None):
    if Titulo is not None:
        query = {"Titulo_Pelicula": Titulo}
        document = collections.find_one(query)
        print(document)
    else:
        documents = collections.find()
        for document in documents:
            print(document)


def create_peliculas(json_peliculas):
    result = collections.insert_one(json_peliculas)
    print(result.inserted_id)


def update_peliculas(id, json_pelicula_update):
    query = {"_id": id}
    new_values = {"$set": json_pelicula_update}
    result = collections.update_one(query, new_values)
    print(result.modified_count)

def delete_peliculas(Titulo=None):
    if Titulo is not None:
        query = {"Titulo_Pelicula": Titulo}
        document = collections.delete_one(query)
        print(document)
    else:
        documents = collections.find()
        for document in documents:
            print(document)






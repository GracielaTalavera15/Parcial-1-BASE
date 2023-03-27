
def create_json_peliculas():
    _id = input("Ingrese el id unico de la pelicula: ")
    Titulo_Pelicula = input("Ingrese el nombre de la nueva pelicula: ")
    Fecha_de_emision = input("Año de lanzamiento de la pelicula: ")
    Genero = input("Genero de la pelicula: ")
    Disponibilidad = input("Rango disponible: ")

    pelicula = {
        "_id": _id,
        "Titulo_Pelicula ": Titulo_Pelicula,
        "Fecha_de_emision ": Fecha_de_emision,
        "Genero ": Genero,
        "Disponibilidad ": Disponibilidad
    }

    return pelicula

def create_json_update():
    print("Menu de opciones para la actualizacion de las peliculas: ")
    print("")
    print("1) Modificar todos los datos")
    print("2) Modificar solo un dato")

    opcion = input("Ingrese una opcion: ")
    if opcion == "1":
        _id = input("Ingrese el id unico de la pelicula: ")
        Titulo_Pelicula = input("Ingrese el nombre de la nueva pelicula: ")
        Fecha_de_emision = input("Año de lanzamiento de la pelicula: ")
        Genero = input("Genero de la pelicula: ")
        Disponibilidad = input("Rango disponible: ")

        pelicula = {
            "_id ": _id,
            "Titulo_Pelicula ": Titulo_Pelicula,
            "Fecha_de_emision ": Fecha_de_emision,
            "Genero ": Genero,
            "Disponibilidad ": Disponibilidad
        }
        return pelicula

    elif opcion == "2":
        indice = input("Ingrese el indice: ")
        valor = input("Ingrese el valor a modificar: ")
        pelicula = {indice: valor}
        return pelicula
    else:
        print("El dato ingresado no es valido")




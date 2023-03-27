import pymongo
from crud import *
from funciones import *

while True:
    print("///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
    print("")
    print("---Bienvenidos a la aplicacion de Graciela---")
    print("")
    print("Menu de opciones:")
    print("1) Ver todas las peliculas:")
    print("2) Consulte una pelicula, ingresando su nombre:")
    print("3) Crear los datos de la nueva pelicula:")
    print("4) Modificar Pelicula:")
    print("5) Eliminar pelicula:")
    print("6) Salir del sistema.")
    print("")
    opcion = input("Ingrese una opcion: ")
    if opcion =="1":
        read_peliculas()
    elif opcion == "2":
        Titulo = input("Ingrese el nombre de la pelicula: ")
        read_peliculas(Titulo)
    elif opcion == "3":
        pelicula = create_json_peliculas()
        create_peliculas(pelicula)
    elif opcion == "4":
        id = int(input("Ingrese el ID a Modificar: "))
        pelicula = create_json_update()
        update_peliculas(id, pelicula)
    elif opcion == "5":
        Titulo = input("Ingrese el nombre de la pelicula que se desea eliminar: ")
        delete_peliculas(Titulo)
    elif opcion == "6":
        print("Saliendo del sistema......")
        break










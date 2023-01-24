# Laboratorio 1 - Inteligencia Artificial
# Integrantes:
#   Jose Miguel Gonzalez 20335
#   Roberto Vallecillos
#   Diego Perdomo

from bdsearch import *
from imgPixel import imgPixel


def main():

    imagen = "prueba.png"
    print(imgPixel(imagen))

    menu = True
    while menu:
        print("------------Menu------------")
        print("1. Graph-Search")
        print("2. Depth-First-Search")
        print("3. Exit")
        option = int(input("Select an option: "))

        if option == 1:
            print("Graph-Search")
            # Aqui va donde llamamos a la funcion de graph-search
        elif option == 2:
            print("Depth-First-Search")
            # Aqui va donde llamamos a la funcion de depth-first-search
        elif option == 3:
            menu = False
            print("Exit")
            # exit
        else:
            print("Invalid option")
            # show the menu again
        print("----------------------------")


main()

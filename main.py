# Laboratorio 1 - Inteligencia Artificial
# Integrantes:
#   Jose Miguel Gonzalez 20335
#   Roberto Vallecillos
#   Diego Perdomo

from bdsearch import *
from imgPixel import imgPixel, matrixImage


def main():

    imagen1 = "prueba1.png"
    imagen2 = "prueba2.png"
    imagen3 = "prueba3.png"
    matrix, entrada, salida = imgPixel(imagen1)

    for i in range(len(matrix)):
        print(matrix[i])

    matrixImage(matrix, "pruebaPixel.png")

    menu = True
    while menu:
        print("------------Menu------------")
        print("1. Graph-Search")
        print("2. Breadth-First-Search")
        print("3. Depth-First-Search")
        print("4. Exit")
        option = int(input("Select an option: "))

        if option == 1:
            print("Graph-Search")
            # Aqui va donde llamamos a la funcion de graph-search
        elif option == 2:
            print("Bredth-First-Search")
            breadth = breadth_first(matrix)
            print(breadth.algoritmo())
            print(breadth.search())
            print(breadth.matrix)
            matrixImage(breadth.matrix, "breadth.png")
        elif option == 3:
            print("Depth-First-Search")
            depth = depth_first(matrix)
            print(depth.algoritmo())
            print(depth.search())
            print(depth.matrix)
            matrixImage(depth.matrix, "depth.png")
            # Aqui va donde llamamos a la funcion de depth-first-search
        elif option == 4:
            menu = False
            print("Exit")
            # exit
        else:
            print("Invalid option")
            # show the menu again
        print("----------------------------")


main()

# Laboratorio 1 - Inteligencia Artificial
# Integrantes:
#   Jose Miguel Gonzalez 20335
#   Roberto Vallecillos
#   Diego Perdomo

from bdsearch import *
from imgPixel import imgPixel, matrixImage


def main():

    imagen = "prueba.png"
    matrix, entrada, salida = imgPixel(imagen)

    # print("Entrada: ", entrada)
    # print("Salida: ", salida)
    # for i in range(len(matrix)):
    #     print(matrix[i])

    resultadoF = matrixImage(matrix)
    # print("Resultado: ", resultadoF)

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
            temp = breadth.matrix
            print(temp)
            for i in range(len(temp)):
                print(temp[i])
        elif option == 3:
            print("Depth-First-Search")
            depth = depth_first(matrix)
            print(depth.algoritmo())
            print(depth.search())
            print(depth.matrix)
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

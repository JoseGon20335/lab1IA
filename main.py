# Laboratorio 1 - Inteligencia Artificial
# Integrantes:
#   Jose Miguel Gonzalez 20335
#   Roberto Vallecillos
#   Diego Perdomo

from bdsearch import *
from imgPixel import imgPixel


def main():

    imagen = "prueba.png"
    imgPixel(imagen)
    matrix = []
    salida = []
    entrada = 0
    for y in range(0,len(x),10):
      temp = []
      for z in range(0,len(x),10):
        if x[y][z][0] == x[y][z][1] and x[y][z][0] >= 225:
          temp.append(0)
        elif x[y][z][1] >= 250 and x[y][z][0] <= 20:
          temp.append(0)
          salida.append((int(z/10),int(y/10)))
        elif x[y][z][0] >= 250 and x[y][z][1] <= 20:
          temp.append(0)
          entrada = (int(z/10),int(y/10))
        else: 
          temp.append(1)
      matrix.append(temp)

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
            print("Bredth-First-Search")
            breadth = breadth_first(matrix,entrada, salida)
            print(breadth.algoritmo())
            print(breadth.search())
            print(breadth.matrix)
         elif option == 3:
            print("Bredth-First-Search")
            depth = depth_first(matrix,entrada, salida)
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

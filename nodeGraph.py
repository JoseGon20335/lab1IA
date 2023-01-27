# Heurísticas

# Manhattan

def manhattan(x1, y1, x2, y2, D = 1):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return D * (dx + dy)


# Diagonal

def Diagonal(x1, y1, x2, y2, D = 1):
        #return abs(x1 - x2) + abs(y1 - y2)
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        #return (dx + dy) * D 
        return (dx + dy) * D + (D * 2 - 2 * D) * min(dx, dy)


# Description: Implementación de un grafo de nodos para el algoritmo A*

class Node():
    
    def __init__(self, pos = None, parent = None):
        self.pos = pos #posición del nodo
        self.parent = parent #nodo padre, osea el previo al actual
        self.g = 0 #costo del camino desde el nodo inicial hasta el actual
        self.h = 0 #heurística del nodo actual hasta el nodo final
        self.f = 0 #f = g + h

    def __eq__(self, other):
        return self.pos == other.pos


    def setH(self, end, heuristic):
        if heuristic == "manhattan":
            self.h = manhattan(self.pos[0], self.pos[1], end[0], end[1])
        elif heuristic == "diagonal":
            self.h = Diagonal(self.pos[0], self.pos[1], end[0], end[1])
        self.f = self.g + self.h



# Algoritmo A*


def astar_3(m, s, es, h = "manhattan"):
    n_i = Node(s, None)
    paths = []

    for e in es:
        #movimientos posibles: derecha, izquierda, arriba, abajo

        #paso 1: nodo inicial

        #nodo inicial
        n_i.setH(e, h)
        n_actual = n_i


        #lista de nodos
        nodes = []
        nodes.append(n_i)

        #nodo con menor f
        lowest_f = [n_i.f, n_i.pos]

        #print(e)
        #print(n_actual.pos)
        #print("------------------")

        
        while n_actual.pos != e:

            #nodo actual y su movimiento
            for move in [(1,0), (-1,0), (0,-1), (0,1) ]:

                #print("checkpoint 1")

                #paso 2: calcular posicion actual

                #calcular posicion actual después de un movimiento
                pos_actual = (n_actual.pos[0] + move[0], n_actual.pos[1] + move[1])
                
                #si la posicion actual esta fuera del mapa, no se agrega
                if pos_actual[0] > (len(m) - 1) or pos_actual[0] < 0 or pos_actual[1] > (len(m[len(m) - 1]) - 1) or pos_actual[1] < 0:
                    continue
                
                # depricated
                #if m[pos_actual[0]][pos_actual[1]] != 0:
                #    continue

                if m[pos_actual[0]][pos_actual[1]] == 0 or m[pos_actual[0]][pos_actual[1]] == 2 or m[pos_actual[0]][pos_actual[1]] == 3:
                    #print("checkpoint 2")

                    #paso 3: calcular g, h y f y agregar a la lista de nodos o no

                    g = n_actual.g + 1
                    heu = 0
                    if h == "manhattan":
                        heu = manhattan(pos_actual[0], pos_actual[1], e[0], e[1])
                    else:
                        heu = Diagonal(pos_actual[0], pos_actual[1], e[0], e[1])
                    f = g + heu

                    #print("\n")
                    #for n in nodes:
                    #    print(n.pos)


                    #print("checkpoint 3")

                    # si la posicion actual ya esta en la lista de nodos, se actualiza el f si es menor
                    i = 0
                    while i < len(nodes):
                        if nodes[i].pos == pos_actual:
                            if nodes[i].f > f:
                                nodes[i].f = f
                            else:
                                i += 1
                        else:
                            i += 1

                    #print("checkpoint 4")

                    #si la posicion actual no esta en la lista de nodos, se agrega
                    new_node = Node(pos_actual, n_actual.pos)
                    new_node.g = n_actual.g + 1
                    new_node.setH(e, h)
                    nodes.append(new_node)

            # paso 4: seleccionar el nodo con menor f


            #print("checkpoint 5")

            # problema con la actualización de lowest_f y n_actual

            #seleccionar el nodo con menor f
            #lowest_f = [nodes[0].f, nodes[0].pos]
            for node in nodes:
                #print(" - lowest: ",lowest_f[1], lowest_f[0])
                #print(" - node: ",node.pos, node.f)
                if node.f <= lowest_f[0] and node.pos != n_actual.pos:
                    lowest_f = [node.f, node.pos]
                    break


            #print("checkpoint 6")
            #paso 5: actualizar el nodo actual
            #n_actual = lowest_f[1]
            for node in nodes:
                if node.pos == lowest_f[1]:
                    n_actual = node
            
            print(n_actual.pos)

        #paso 6: construir el camino
        print(nodes)
        path = []
        current = n_actual
        while current is not None:
            path.append(current.pos)
            current = current.parent
        paths.append(path[::-1])
    return paths


            





# Prueba

def main():
    maze = [
         [3, 0, 0, 0, 3, 0],
         [0, 1, 1, 1, 1, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 0],
         [0, 1, 0, 2, 1, 0],
         [0, 0, 0, 0, 0, 0]
    ]
    #start = None
    #end = None
    #for i in range(len(maze)):
    #    for j in range(len(maze[i])):
    #        if maze[i][j] == 2:
    #            start = (i, j)
    #        if maze[i][j] == 3:
    #            end = (i, j)


    #maze = [[0, 0, 2, 0, 0, 0, 0, 0],
    #        [0, 1, 1, 1, 0, 1, 1, 0],
    #        [0, 1, 0, 0, 0, 0, 1, 0],
    #        [0, 1, 0, 1, 1, 0, 1, 0],
    #        [0, 1, 0, 0, 1, 0, 1, 3],
    #        [0, 0, 0, 0, 0, 0, 1, 0],
    #        [1, 1, 0, 1, 1, 0, 1, 0],
    #        [0, 0, 0, 3, 0, 0, 0, 0]]
    #start = (0, 2)
    #end = (7, 4)

    start = None
    end = []

    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 2:
                start = (i, j)
            if maze[i][j] == 3:
                end.append((i, j))

    #formato de coordenadas y,x

    #print(start)
    #print(end)
#
    path = astar_3(maze, start, end, "manhattan")

    print(path)

    #path =  astar2(maze, start, end)




    #path = astar(maze, start, end, "manhattan")
#
    #print("----------------------------------------------------")
#
    #print(path)

    #path = astar(maze, start, end, "diagonal")
#
    #print("----------------------------------------------------")
    #print(path)
#

main()
            









#Aún odio mi vida
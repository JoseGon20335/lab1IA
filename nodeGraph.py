
# Description: Implementación de un grafo de nodos para el algoritmo A*

class Node():
    
    def __init__(self, pos = None, parent = None):
        self.pos = pos
        self.parent = None
        self.g = 0
        self.h = 0
        self.f = 0

    def __eq__(self, other):
        return self.pos == other.pos


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


# Algoritmo A*

def astar(maze, start, end, heuristic = "manhattan"):
    node_i = Node(start, None)
    node_f = Node(end, None)

    _open = []
    _closed = []

    _open.append(node_i)
    #print("open: ", _open[0].pos , " , ",  _open[0].parent) 
    print(_open)
    print(_closed)
    #print
    #print("closed: ", _closed[0].pos , " , ",  _closed[0].parent)


    while len(_open) > 0:
        #print("entrando al while")

        node_c = _open[0]
        node_c_index = 0
        for i, item in enumerate(_open):
            if item.f < node_c.f:
                node_c = item
                node_c_index = i

        _open.pop(node_c_index)
        _closed.append(node_c)

        #rint(" still alive")

        if node_c == node_f:
            path = []
            current = node_c
            while current is not None:
                path.append(current.pos)
                current = current.parent
            return path[::-1]

        
        print(node_c.pos)
        print(node_f.pos)

        sons = []

        #movimientos posibles
        # diagonal no permitida

        for n in [(0, -1), (0, 1), (-1, 0), (1, 0)]:

        #for n in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:

            # 0 = camino libre
            # 1 = pared
            # 2 = inicio
            # 3 = fin

            node_pos = (node_c.pos[0] + n[0], node_c.pos[1] + n[1])




            if node_pos[0] > (len(maze) - 1) or node_pos[0] < 0 or node_pos[1] > (len(maze[len(maze) - 1]) - 1) or node_pos[1] < 0:
                continue

            if maze[node_pos[0]][node_pos[1]] != 0:
                continue

            new_node = Node(node_pos, node_c)

            sons.append(new_node)

        #print("sons: ", sons)
        #for e in sons: 
            #print(e.pos, " , ", e.parent.pos, " , ", e.g, " , ", e.h, " , ", e.f)
        print("*******************************************************")
        for e in sons:
            print(e.pos)

        print("*******************************************************")

        for son in sons:
            
            for cs in _closed:
                if son == cs:
                    continue

            son.g = node_c.g + 1
            if heuristic == "manhattan":
                son.h = manhattan(son.pos[0], son.pos[1], node_f.pos[0], node_f.pos[1])
            else:
                son.h = Diagonal(son.pos[0], son.pos[1], node_f.pos[0], node_f.pos[1])
            son.f = son.g + son.h

            for op in _open:
                if son == op and son.g > op.g:
                    continue

            _open.append(son)

# Prueba

def main():
   # maze = [
   #     [3, 0, 0, 0, 3, 0],
   #     [0, 1, 1, 1, 1, 0],
   #     [0, 1, 0, 0, 1, 0],
   #     [0, 1, 0, 0, 1, 0],
   #     [0, 1, 0, 2, 1, 0],
   #     [0, 0, 0, 0, 0, 0]
   # ]
#
   # start = None
   # end = None
#
#
   # for i in range(len(maze)):
   #     for j in range(len(maze[i])):
   #         if maze[i][j] == 2:
   #             start = (i, j)
   #         if maze[i][j] == 3:
   #             end = (i, j)


    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
            
    start = (0, 0)
    end = (7, 6)

    print(start)
    print(end)




    path = astar(maze, start, end, "manhattan")

    print("----------------------------------------------------")

    print(path)

    #path = astar(maze, start, end, "diagonal")
#
    #print("----------------------------------------------------")
    #print(path)
#

main()
            









#Aún odio mi vida
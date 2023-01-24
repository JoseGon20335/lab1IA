from collections import deque
from abc import ABC, abstractmethod


matrixx = [[0,0,0,0,0],
          [1,0,1,1,0],
          [0,0,1,0,0],
          [0,1,0,0,1],
          [0,0,0,0,0],
                     ]

def search(start, camino, graph):
  space = []
  temp = start
  for x in camino:
    lista = graph[temp]
    for y in lista:
      if y[0] == x:
        temp = y[1]
        space.append(temp)
  space.pop(-1)
  return space


class busqueda(ABC):
  matrix = None
  graph = None

  def __init__(self, matrix):
    self.matrix = matrix
    self.graph = self.grafo()

  def grafo(self):
    alto = len(self.matrix)
    largo = len(self.matrix[0])
    grafo = {(i, j): [] for j in range(largo) for i in range(alto) if not self.matrix[i][j]}
    for par in grafo.keys():
      if par[0]+1 < alto and not self.matrix[par[0]+1][par[1]]:
        grafo[par].append(("S",(par[0]+1, par[1])))
        grafo[(par[0]+1, par[1])].append(("N",par))
      if par[1]+1 < largo and not self.matrix[par[0]][par[1]+1]:
        grafo[par].append(("E", (par[0], par[1]+1)))
        grafo[(par[0], par[1]+1)].append(("O", par))
    return grafo

  @abstractmethod
  def algoritmo(self):
    pass

class breadth_first(busqueda):
  def __init__(self):
    super().__init__(matrixx)

  def algoritmo(self):
    start,end = (0,0),[(4,4), (0,4)]
    cola = deque([("", start)])
    visitado = set()
    while cola:
      camino, current = cola.popleft()
      if current in end:
        return camino
      if current in visitado:
        continue
      visitado.add(current)
      for direction, vecino in self.graph[current]:
        cola.append((camino+direction,vecino))

class depth_first(busqueda):
  def __init__(self):
    super().__init__(matrixx)

  def algoritmo(self):
    start,end = (0,0),[(4,4), (0,4)]
    stack = deque([("", start)])
    visitado = set()
    while stack:
      camino, current = stack.pop()
      if current in end:
        return camino
      if current in visitado:
        continue
      visitado.add(current)
      for direction, vecino in grafo[current]:
        stack.append((camino+direction,vecino))

  

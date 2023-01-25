from collections import deque
from abc import ABC, abstractmethod

class busqueda(ABC):
  matrix = None
  graph = None

  def __init__(self, matrix, start, end):
    self.start = start
    self.end = end
    self.camino = None
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

  def search(self):
    space = []
    temp = self.start
    for x in self.camino:
      lista = self.graph[temp]
      for y in lista:
        if y[0] == x:
          temp = y[1]
          self.matrix[temp[0]][temp[1]] = 4
          space.append(temp)
    self.matrix[temp[0]][temp[1]] = 3  
    space.pop(-1)
    return space


class breadth_first(busqueda):

  def algoritmo(self):
    cola = deque([("", self.start)])
    self.matrix[int(self.start[0])][int(self.start[1])] = 2 
    visitado = set()
    while cola:
      camino, current = cola.popleft()
      if current in self.end:
        self.matrix[current[0]][current[1]] = 3 
        self.camino = camino
        return camino
      if current in visitado:
        continue
      visitado.add(current)
      for direction, vecino in self.graph[current]:
        cola.append((camino+direction,vecino))


class depth_first(busqueda):

  def algoritmo(self):
    stack = deque([("", self.start)])
    self.matrix[int(self.start[0])][int(self.start[1])] = 2 
    visitado = set()
    while stack:
      camino, current = stack.pop()
      if current in self.end:
        self.matrix[current[0]][current[1]] = 3 
        self.camino = camino
        return camino
      if current in visitado:
        continue
      visitado.add(current)
      for direction, vecino in self.graph[current]:
        stack.append((camino+direction,vecino))


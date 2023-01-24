''' class Node():
    
    def __init__(value):
        self.value = value
        self.left = None
        self.right = None
        self.up = None
        self.down = None


class Graph():

    def __init__(self, nodes):
        self.nodes = []
        self.addNodes(nodes)

    def addNodes(self, nodes):
        i = 0
        j = 0
        for i in range(len(nodes)):
            for j in range(len(nodes[i])):
                if nodes[i][j] == 0:
                    self.nodes.append(Node((i, j)))

    
 '''


#Odio mi vida


'''
    Date   : 17/11/2020
    Day    : Tuesday
    Author : Md. Aminul Islam
    E-mail : aminulbrur8@gmail.com
    Subject: Algorithm: Graph Theory
    Topic  : Adjacency List Representation
    LInk   : https://runestone.academy/runestone/books/published/pythonds/Graphs/Implementation.html
'''

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight
        
    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.verlist = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.verlist[key]  = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.verlist:
            return self.verlist[n]
        else:
            return None
    
    def __contains__(self, n):
        return n in self.verlist
    
    def addEdge(self, f, t, weight=0):
        if f not in self.verlist:
            nv = self.addVertex(f)
        if t not in self.verlist:
            nv = self.addVertex(t)
        self.verlist[f].addNeighbor(self.verlist[t], weight)
    
    def getVertices(self):
        return self.verlist.keys()
    
    def __iter__(self):
        return iter(self.verlist.values())



g = Graph()
for i in range(6):
    g.addVertex(i)

g.verlist

g.addEdge(0, 1, 5)
g.addEdge(0, 5, 2)
g.addEdge(1, 2, 4)
g.addEdge(2, 3, 9)
g.addEdge(3, 4, 7)
g.addEdge(3, 5, 3)
g.addEdge(4, 0, 1)
g.addEdge(5, 4, 8)
g.addEdge(5, 2, 1)

for v in g:
    for w in v.getConnections():
        print("( %s , %s )" % (v.getId(), w.getId()))
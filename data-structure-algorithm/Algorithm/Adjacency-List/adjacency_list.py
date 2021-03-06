'''
    Date   : 17/11/2020
    Day    : Tuesday
    Author : Md. Aminul Islam
    E-mail : aminulbrur8@gmail.com
    Subject: Algorithm: Graph Theory
    Topic  : Adjacency List Representation
    LInk   : https://www.programiz.com/dsa/graph-adjacency-list
'''

# graph = {
#     'A': set(['B', 'C']),
#     'B': set(['A', 'D', 'E']),
#     'C': set(['A', 'F']),
#     'D': set(['B', 'F']),
#     'F': set(['C', 'E'])
# }

# print(graph)

### Adjacency List representation
class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None

class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(d)
        node.next = self.graph[d]
        self.graph[d] = node

    # Print the graph
    def print_agraph(self):
        for i in range(self.V):
            print("Vertex " + str(i) + ":", end="")
            temp = self.graph[i]
            while temp:
                print(" -> {}".format(temp.vertex), end="")
                temp = temp.next
            print(" \n")

    
if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(0, 3)
    graph.add_edge(1, 2)

    graph.print_agraph()
'''
    Date   : 18/11/2020
    Day    : Wednessday
    Author : Md. Aminul Islam
    E-mail : aminulbrur8@gmail.com
    Subject: Algorithm: Graph Theory
    Topic  : Breadth First Traversal or Breadth First Search (BFS)
    LInk   : https://www.educative.io/edpresso/how-to-implement-a-breadth-first-search-in-python
'''

# BFS Algorithm
def bfs(graph, node, visited):
    queue = []
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for nieghbour in graph[s]:
            if nieghbour not in visited:
                visited.append(nieghbour)
                queue.append(nieghbour)
    print()

# Driver Code
graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

graph1 = {0: [1, 2], 1: [2, 5], 2: [3, 4], 3: [2, 4], 4: [5], 5: []}

bfs(graph, 'A', visited=[])
bfs(graph1, 0, visited=[])
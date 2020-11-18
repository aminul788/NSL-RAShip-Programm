'''
    Date   : 18/11/2020
    Day    : Wednessday
    Author : Md. Aminul Islam
    E-mail : aminulbrur8@gmail.com
    Subject: Algorithm: Graph Theory
    Topic  : Depth First Traversal/Search
    LInk   : https://www.educative.io/edpresso/how-to-implement-depth-first-search-in-python
'''




# DFS Algorithm
def dfs(graph, node, visited):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(graph, neighbour, visited)   

# Driver Code
# Using a Pyhton dictionary to act as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

graph1 = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

dfs(graph, 'A', visited=set())
print()
dfs(graph1, '1', visited=set())
print()
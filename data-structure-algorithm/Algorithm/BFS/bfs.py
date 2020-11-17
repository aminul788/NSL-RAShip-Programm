'''
    Date   : 17/11/2020
    Day    : Tuesday
    Author : Md. Aminul Islam
    E-mail : aminulbrur8@gmail.com
    Subject: Algorithm: Graph Theory
    Topic  : Breadth First Traversal or Breadth First Search (BFS)
    LInk   : https://www.programiz.com/dsa/graph-bfs
'''

import collections

## BFS Algorithm
def bfs(graph, root):
    visited, queue = set(), collections.deque([root])
    visited.add(root)


    while queue:
        # Dequeue0 a vertex from queue
        vertex = queue.popleft()
        print(str(vertex) + " ", end="")

        # If not visited, mark it as visited, and enqueue it
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    print("\n")

if __name__ == "__main__":
    graph = {0: [1, 2], 1: [2, 5], 2: [3, 4], 3: [2, 4], 4: [5], 5: []}
    print("Following is Breadth First Traversal/Search: ")
    bfs(graph, 0)
from collections import deque

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = []

    def add_edge(self, vertex_1, vertex_2):
        self.adjacency_list[vertex_1].append(vertex_2)
        self.adjacency_list[vertex_2].append(vertex_1)
    
    def dfs_recursive(self, start):
        results = []
        memory = {}
        def dfs(start):
            if not start:
                return
            
            results.append(start)
            memory[start] = True

            for vertex in self.adjacency_list[start]:
                if vertex not in memory:
                    return dfs(vertex)

        dfs(start)
        return results

    def dfs_iterative(self, start):
        results = []
        stack = []
        memory = {}

        stack.append(start)
        memory[start] = True

        while stack:
            current = stack.pop()
            results.append(current)

            for vertex in self.adjacency_list[current]:
                if vertex not in memory:
                    stack.append(vertex)
                    memory[vertex] = True
        return results
    
    def bfs_iterative(self, start):
        results = []
        memory = {}
        queue = deque()

        queue.append(start)
        memory[start] = True

        while queue:
            current = queue.popleft()
            results.append(current)

            for vertex in self.adjacency_list[current]:
                if vertex not in memory:
                    queue.append(vertex)
                    memory[vertex] = True

        return results

graph = Graph()
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')
graph.add_vertex('F')
graph.add_vertex('G')
graph.add_edge('A', 'B')
graph.add_edge('A', 'D')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('C', 'G')
graph.add_edge('C', 'E')
graph.add_edge('F', 'D')
graph.add_edge('F', 'E')
print(graph.dfs_iterative('A'))
print(graph.dfs_recursive('A'))
print(graph.bfs_iterative('A'))
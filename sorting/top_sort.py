from collections import defaultdict, deque


class Graph:
    """Represents a directed, acyclic graph."""

    def __init__(self, edge_list):
        """Initializes a Graph with edges."""

        self.graph = self.create_graph(edge_list)
        self.all_nodes = list(self.graph.keys())

    def create_graph(self, edge_list):
        """Creates a dictionary representation of a graph from the edge list."""

        graph = defaultdict(list)
        for edge in edge_list:
            if len(edge) > 1:
                a, b = edge
                # In a directed graph, append 'a' to 'b's adjacency list
                graph[b].append(a)
            else:
                a = edge[0]
                # If there is no edge, still add the node to the graph
                graph[a] = graph.get(a, [])
        return graph

    def sort(self):
        """Returns a topological sort of the graph using Depth-First Search. Raises a ValueError if a cycle is detected."""

        result = deque()
        visited = set()
        visiting = set()

        def dfs(vertex):
            """Helper function to perform a Depth-First Search."""

            visiting.add(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor in visited:
                    continue
                if neighbor in visiting:
                    # A cycle is detected
                    raise ValueError("A cycle detected in the graph.")
                dfs(neighbor)
            # Once all neighbors are visited, remove the vertex from visiting set and add to visited set
            visiting.remove(vertex)
            visited.add(vertex)
            # Add vertex to the result
            result.appendleft(vertex)

        # Start DFS for each unvisited vertex
        for vertex in self.all_nodes:
            if vertex not in visited:
                dfs(vertex)
        # Returns a queue of the topological sort, but can be converted to a list if needed
        return result


if __name__ == "__main__":

    edge_list = [
        ["u"],
        ["v", "w"],
        ["w", "z"],
        ["x", "u"],
        ["y", "v"],
        ["z"],
    ]
    
    graph = Graph(edge_list)

    try:
        print(graph.sort())  # deque(['z', 'w', 'v', 'y', 'u', 'x'])
    except ValueError as e:
        print(e)

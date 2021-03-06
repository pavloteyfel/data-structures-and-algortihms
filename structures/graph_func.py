"""Graph related topics"""
from collections import deque


def create_graph(edges: list[tuple[str, str]]) -> dict:
    """Create graph structure from edge list"""
    graph = {}
    for a, b in edges:
        if a not in graph:
            graph[a] = []
        graph[a].append(b)
        if b not in graph:
            graph[b] = []
        graph[b].append(a)
    return graph


def traversal(graph: dict[str, str], node: str) -> list:
    """Simple graph traversal"""
    memo: set = set()
    node_list: list = []

    def _traveral(graph: dict[str, str], node: str, memo: set, node_list: list) -> list:
        """Inner recursive graph traversal"""
        node_list.append(node)
        memo.add(node)
        for neighbour in graph[node]:
            if neighbour not in memo:
                _traveral(graph, neighbour, memo, node_list)
        return node_list

    return _traveral(graph, node, memo, node_list)


def count_components(edge: list[tuple[str, str]]) -> int:
    """Counts the individual components inside a graph"""
    count: int = 0
    memo: set = set()
    graph: dict = create_graph(edge)
    for node in graph:
        if explore(graph, node, memo):
            count += 1
    return count


def explore(graph: dict[str, str], node: str, memo: set) -> bool:
    """Return true after explored all the connected nodes"""
    if node in memo:
        return False
    memo.add(node)
    for neighbour in graph[node]:
        if neighbour not in memo:
            explore(graph, neighbour, memo)
    return True


def shortest_neighbour(edges, src, dst):
    """Return shortest path between two nodes"""
    graph = create_graph(edges)
    queue = deque()
    memo = set()

    queue.append((src, 0))
    memo.add(src)

    while queue:
        node, distance = queue.popleft()

        if node == dst:
            return distance

        for vertex in graph[node]:
            if vertex not in memo:
                queue.append((vertex, distance + 1))
                memo.add(vertex)

    return None


def in_boundry(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[row])


def explore_coord(grid, row, col, memo):
    if not in_boundry(grid, row, col):
        return False

    if grid[row][col] == 0:
        return False

    if (row, col) in memo:
        return False

    memo.add((row, col))

    explore_coord(grid, row + 1, col, memo)
    explore_coord(grid, row - 1, col, memo)
    explore_coord(grid, row, col + 1, memo)
    explore_coord(grid, row, col - 1, memo)

    return True


def island_counter(grid):
    counter = 0
    memo = set()

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if explore_coord(grid, row, col, memo):
                counter += 1

    return counter


my_edges = [
    ("i", "j"),
    ("k", "i"),
    ("m", "k"),
    ("k", "l"),
    ("o", "n"),
]


grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 1],
    [1, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
]


assert island_counter(grid) == 4
assert shortest_neighbour(my_edges, "m", "j") == 3
assert count_components(my_edges) == 2

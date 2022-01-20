def count_nodes(edges):
    graph = create_graph(edges)
    count = 0
    memo = set()

    for node in graph:
        count += find_component(graph, node, memo)

    return count


def create_graph(edges):
    graph = {}
    for node_1, node_2 in edges:
        if node_1 not in graph:
            graph[node_1] = []
        graph[node_1].append(node_2)
        if node_2 not in graph:
            graph[node_2] = []
        graph[node_2].append(node_1)
    return graph


def find_component(graph, node, memo):
    if node in memo:
        return 0

    memo.add(node)
    size = 1

    for neighbour in graph[node]:
        size += find_component(graph, neighbour, memo)

    return size


edges = [
    ("i", "j"),
    ("k", "i"),
    ("m", "k"),
    ("k", "l"),
    ("o", "n"),
]

assert count_nodes(edges) == 7

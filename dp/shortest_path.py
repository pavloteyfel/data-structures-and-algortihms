from collections import deque

graph = {
    "a": ["b", "d"],
    "b": ["a", "c"],
    "c": ["b", "e"],
    "d": ["e", "a"],
    "e": ["d", "c"],
}


def shortest_path(graph, src, dst):
    queue = deque()
    memo = set()

    queue.append((src, 0))
    memo.add(src)

    while queue:
        node, distance = queue.popleft()

        if node == dst:
            return distance

        for neighbour in graph[node]:
            if neighbour not in memo:
                queue.append((neighbour, distance + 1))
                memo.add(neighbour)

    return -1


print(shortest_path(graph, "a", "c"))

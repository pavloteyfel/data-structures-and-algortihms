def count_island(island_map):
    memo = set()
    count = 0

    for row in range(len(island_map)):
        for col in range(len(island_map[row])):
            if find_island(island_map, row, col, memo):
                count += 1

    return count


def find_island(grid, row, col, memo):
    if not is_valid_coord(grid, row, col):
        return False

    if grid[row][col] == 0:
        return False

    if (row, col) in memo:
        return False

    memo.add((row, col))

    # dfs
    find_island(grid, row + 1, col, memo)
    find_island(grid, row - 1, col, memo)
    find_island(grid, row, col + 1, memo)
    find_island(grid, row, col - 1, memo)

    return True


def is_valid_coord(grid, row, col):
    return 0 <= row < len(grid) and 0 <= col < len(grid[row])


island_map = [
    [1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
]

assert count_island(island_map) == 4

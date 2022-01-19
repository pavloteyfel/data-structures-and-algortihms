def can_sum(array, k):
    size = k + 1
    tabulator = [False] * size
    tabulator[0] = True
    for i, value in enumerate(tabulator):
        if value:
            for j in array:
                if i + j < size:
                    tabulator[i + j] = True
    return tabulator[size - 1]


assert can_sum([4, 8, 9, 2], 11) == True

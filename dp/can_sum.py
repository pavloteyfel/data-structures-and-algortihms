def can_sum(array, k):
    size = k + 1
    tabulator = [False] * size
    tabulator[0] = True
    for i, value in enumerate(tabulator):
        if value:
            for j in array:
                if i+j < size:
                    tabulator[i+j] = True
                    print(tabulator)
    return tabulator[size-1]


a = [1, 2, 3, 4]
a[10] = 7

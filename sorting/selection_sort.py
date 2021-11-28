def selection_sort(array):
    smallest = 0
    size = len(array)
    start = 0
    for i in range(start, size):
        for j in range(size):
            if array[j] < array[smallest]:
                smallest = j
        array[0] = array[smallest]
        start += 1
    return array

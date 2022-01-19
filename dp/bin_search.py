def binary_search(array, value):
    left = 0
    right = len(array) - 1

    while left <= right:
        # // means we take the floor value 0 + 5 = 5 / 2 = 2.5 -> 2
        middle = (left + right) // 2 
        if array[middle] == value:
            return middle

        if array[middle] > value:
            right = middle - 1
        else:
            left = middle + 1
    return -1

assert binary_search([10, 13, 28, 44, 63], 44) == 3
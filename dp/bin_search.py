
array = [10, 13, 28, 44, 63]



def search(array, value):
    left = 0
    right = len(array) - 1

    while left <= right:
        middle = (left + right) // 2 # // means we take the floor value 0 + 5 = 5 / 2 = 2.5 -> 2

        if array[middle] == value:
            return middle

        if array[middle] > value:
            right = middle - 1
        else:
            left = middle + 1
    return -1


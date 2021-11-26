sample = [2,6,4,1,7,4,8,3,3]

def bubble_sort(array):
    size = len(array)
    for i in range(size):
        for j in range(size-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

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

def insertion(array):
    for pointer in range(1, len(array)):
        if array[pointer-1] > array[pointer]:
            step = pointer
            while step > 0 and array[step-1] > array[step]:
                array[step-1], array[step] = array[step], array[step-1]
                step -= 1
    return array




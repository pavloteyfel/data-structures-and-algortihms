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

def insertion_sort(arr):
    for key in range(1, len(arr)):
        if arr[key] < arr[key-1]:
            j = key
            while j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1
    return arr


# print(bubble_sort(sample))
# print(selection_sort(sample))
print(insertion_sort(sample))

import math

print(math.log2(5000)*5000)
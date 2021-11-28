def insertion_sort(array):
    for pointer in range(1, len(array)):
        if array[pointer-1] > array[pointer]:
            step = pointer
            while step > 0 and array[step-1] > array[step]:
                array[step-1], array[step] = array[step], array[step-1]
                step -= 1
    return array
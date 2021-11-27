def pivot(array, start, end):
    print('received array -> ', array[start:end])
    pivot_value = array[start] # the pivot value always the first number
    swap_index = start

    for i in range(start + 1, end + 1): # we can omit the first number as it is the pivot
        if array[i] < pivot_value:
            swap_index += 1
            swap(array, swap_index, i)

    swap(array, swap_index, start)

    return swap_index    

def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
    return array

def sort(array):
    last_index = len(array) - 1
    def _sort(array, left=0, right=last_index): # to be consistent with the left, start, right, end values
        if left < right:
            pivot_index = pivot(array, left, right)
            _sort(array, left, pivot_index - 1)
            _sort(array, pivot_index + 1, right)
        return array
    return _sort(array)

print(sort([4,3,2,0,7,3]))

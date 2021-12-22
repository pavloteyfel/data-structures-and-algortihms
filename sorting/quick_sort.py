def swap(array, i, j ):
    array[i], array[j] = array[j], array[i]

def pivot(array, start, end):
    pivot_index = start
    swap_index = start
    for i in range(start + 1, end + 1):
        if array[i] < array[pivot_index]:
            swap_index += 1
            swap(array, i, swap_index)
    swap(array, pivot_index, swap_index)
    return swap_index

def quick_sort(array):
    def sort(array, left, right):
        if left < right:
            pivot_index = pivot(array, left, right)
            sort(array, left, pivot_index - 1)
            sort(array, pivot_index + 1, right)
        return array
    return sort(array, 0, len(array) - 1)


assert quick_sort([4, 6, 3, 1, 2, 8, 9]) == [1, 2, 3, 4, 6, 8, 9]
assert quick_sort([3,1,2]) == [1,2,3]
assert quick_sort([1]) == [1]
assert quick_sort([]) == []

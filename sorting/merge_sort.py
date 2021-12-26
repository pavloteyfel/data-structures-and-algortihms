def merge_sort(array):
    if len(array) == 1:
        return array
    index = len(array) // 2
    left = array[:index]
    right = array[index:]
    return merge(merge_sort(left), merge_sort(right))


def merge(array1, array2):
    result = sorted(array1 + array2)
    return result

# One liner for fun


def sort(arr):
    return arr if (l := len(arr)) == 1 else sorted(sort(arr[:l//2]) + sort(arr[l//2:]))

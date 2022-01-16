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


def merge_sort_v2(arr):
    return (
        arr
        if (l := len(arr)) == 1
        else sorted(merge_sort_v2(arr[: l // 2]) + merge_sort_v2(arr[l // 2 :]))
    )

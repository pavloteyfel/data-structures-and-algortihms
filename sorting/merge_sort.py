def merge_sort(array):
    if len(array) == 1:
        return array
    print('to divide -> ', array)
    index = len(array) // 2
    left = array[:index]
    right = array[index:]
    print('divided -> ', left, '<>' ,right)
    return merge(merge_sort(left), merge_sort(right))

def merge(array1, array2):
    print('to merge -> ', array1, '&', array2)
    result = sorted(array1 + array2)
    print('merged -> ', result)
    return result

print(merge_sort([6,3,7,4,1,9,8]))

# Demonstrate the usage of sliding window technique

def max_subarray(array, k):
    max_sum = 0
    curr_sum = 0

    for i in range(k):
        max_sum += array[i]
    
    curr_sum = max_sum

    for j in range(k, len(array)):
        curr_sum = curr_sum + array[j] - array[j-k]
        max_sum = max(max_sum, curr_sum)
    
    return max_sum



assert max_subarray([2,6,9,2,1,8,5,6,3], 3) == 19
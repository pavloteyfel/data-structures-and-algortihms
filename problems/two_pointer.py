# Demonstrate the two pointer technique

def zero_sum(array):
    """Finds two indices where the sum is zero, only works with sorted arrays"""
    left = 0
    right = len(array) - 1

    while left < right:
        num_sum = array[left] + array[right]

        if num_sum == 0:
            return left, right
        
        if num_sum > 0:
            right -= 1
        else:
            left += 1
    
    return None, None


def count_uniuqe(array):
    left = 0
    right = 1

    while right < len(array):
        if array[right] != array[left]:
            left += 1
            array[left] = array[right]
        right += 1

    return left + 1

assert zero_sum([-3, -1, 0, 1, 2, 4]) == (1, 3)
assert count_uniuqe([-1, -1, 0, 1, 2, 2, 3, 4, 4, 4]) == 6
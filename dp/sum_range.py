def sum_range(n):
    """
    Recursive funtion that sums up all numbers found from 0 to the nth
    number provided as an argument to the function

    >_ sum_range(3) will return 6, as 1+2+3=6
    """

    # The base case is to return zero if we call sum_range(0)
    if n == 0:
        return 0

    # In any other cases we need to calculate the number based on the n + n-1
    # forumla until we reach zero
    return n + sum_range(n - 1)

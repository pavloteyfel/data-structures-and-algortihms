def factorial(n):
    """
    Function returns factorial of a number n!
    >_ factorial(4) returns 24, as 4*3*2*1=24
    """

    # The base case is 0! = 1, a matematically correct statement, we could
    # optimize this base case a little bit as 1! = 1 and 2! = 2, but this is
    # not the goal here
    if n == 0:
        return 1

    # n! is equal to the n * n-1, until we reach zero: 0! = 1
    return n * factorial(n-1)


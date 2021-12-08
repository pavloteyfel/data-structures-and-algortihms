def filter_odd(array):
    """
    >_ filter_odd([1,2,3,4,5]) -> will return [1,3,5] odd numbers
    """
    # Create an empty list to store the result if the number is odd
    containter = []

    # Base case: if empy list was provided then we are done and need to return
    # an empty list. It could be simplified to:
    # if not array: ...
    if len(array) == 0:
        return containter
    
    # Check if the first number is odd, and put it into container
    if array[0] % 2 != 0:
        containter.append(array[0])
    
    # Python can handle [1:] on an empy list, but I added this check to spare
    # one more unnecessary recursion call
    if len(array) == 1:
        return containter

    # In this phase we probably have something in our container, an odd number
    # or an empy list. Let's concatenate it with the result of the result of 
    # the remaining filtering
    return containter + filter_odd(array[1:])


import math



def p(n,m):
    if m == 0:
        return 1

    if m == 1:
        return n

    if m == -1:
        return 1/n
    
    if m < 0:
        return 1/n * p(n, m+1)

    return n * p(n, m-1)

print(pow(3,-4))
print(p(3,-4))


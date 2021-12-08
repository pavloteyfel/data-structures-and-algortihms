def product(array):
    """Product of array
    >_ product([1,2,3]) -> 6, as 1*2*3=6
    """

    # Our first base case, if there is nothing then return 0
    if not array:
        return 0

    # If we have one element in the array, then we know that the result is the
    # first element
    if len(array) == 1:
        return array[0]
    
    # Here we know that there will be at least 2 elements in the array
    # We slice the first element and send the remaining elements for further
    # processing
    return array[0] * product(array[1:])



def count_down(n):
    """
    Recursive function prints out numbers from n to 0 with 1 step
    >_ count_down(5) will print 5, 4, 3, 2, 1, 0
    """
    
    # Our logic is to print every number that was provided to the function
    # We want zero to be included as well
    print(n)
    
    # Bases case: if zero was provided then we have to stop our function
    if n == 0: return

    # Until zero is not reached, we call the function with n-1 step to reach
    # zero
    count_down(n-1)

def count_down_v2(n, l=[]):
    """
    Recursive function returns a list of numbers from n to 0 with step
    >_ count_down_v2(5) will return a list [5, 4, 3, 2, 1, 0]
    """

    # We put the number in the list
    l.append(n)
    
    # If we reach the end of the counter, then we return the list with all the
    # element collected in the list
    if n == 0:
        return l
    
    # If counter is still in progress, then we decrease the number by 1 and
    # return it to itself with the list for further operations
    return count_down_v2(n-1, l)

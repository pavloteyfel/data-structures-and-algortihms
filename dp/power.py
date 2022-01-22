def power(n, m):
    """
    Function returns the power n^m, it only works if m > 0
    >_ power(2,4) -> 2*2*2*2 = 16
    """
    # Our base case, we always get 1 if the power is 0 regardless the n
    if m == 0:
        return 1

    # We need to decrease the m every time, until we hit 0, in that case we
    # will have 1
    return n * power(n, m - 1)


def power_v2(n, m):
    """
    Function returns the power n^m, works with negative integers as well
    >_ power(2,4) -> 2*2*2*2 = 16
    """
    # Our base case remains, our utlimate goal to reach zero
    if m == 0:
        return 1

    # If we are dealing with negative integers, then the formula changes a
    # little bit: 2^-3 = 1/2 * 1/2 * 1/2 = 1/(2*2*2) = 1/8
    if m < 0:
        return (
            1 / n * power_v2(n, m + 1)
        )  # we have to reach the zero from the negative side
    else:
        return n * power_v2(n, m - 1)

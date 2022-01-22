def fib(n):
    """Return the nth fibonacci number
    >_ fib(3) -> 2, as (0,) 1, 1, 2
    """

    # Our base cases:
    # fib(0) = 0
    # fib(1) = 1
    if n < 2:
        return n

    # Until n=2 we don't know what is the fib number, so we need to find it out
    return fib(n - 1) + fib(n - 2)


def fib2(n):
    if n < 2:
        return n

    x, y = 0, 1

    for _ in range(2, n):
        tmp = x
        x = y
        y = tmp + y

    return y + x

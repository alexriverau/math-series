def fibonacci(n):
    """
    Function returns the nth value in the Fibonacci Series
    """
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci(n - 1) + fibonacci(n - 2)


def lucas(n):
    """
    Function returns the nth value in the Lucas Numbers
    """

    if n == 0:
        return 2

    if n == 1:
        return 1

    return lucas(n - 1) + lucas(n - 2)


def sum_series(n, x=0, y=1):
    """
    Fibonacci Series, n parameter needed.
    Lucas Numbers, optional parameters (2, 1) are needed.
    Any other optional parameters will produce other series.
    """

    if x == 0 and y == 1:
        return fibonacci(n)
    elif x == 2 and y == 1:
        return lucas(n)
    else:
        return 'These optional parameters produce a different series'



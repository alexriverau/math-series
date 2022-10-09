from series import fibonacci, lucas, sum_series

# Fibonacci tests


def test_fibonacci_function():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_wrong():
    actual = fibonacci(1)
    expected = 2
    assert actual != expected


def test_fibonacci_zero():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_one():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_two():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fibonacci_ten():
    actual = fibonacci(10)
    expected = 55
    assert actual == expected


# Lucas tests


def test_lucas_function():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_wrong():
    actual = lucas(1)
    expected = 2
    assert actual != expected


def test_lucas_two():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_lucas_nine():
    actual = lucas(9)
    expected = 76
    assert actual == expected


# sum_series tests


def test_sum_series_function():
    actual = sum_series(1)
    expected = 1
    assert actual == expected


def test_sum_series_fail():
    actual = sum_series(1)
    expected = 100
    assert actual != expected


def test_sum_series_no_optional_params():
    actual = sum_series(5)
    expected = 5
    assert actual == expected


def test_sum_series_lucas_params():
    actual = sum_series(7, 2, 1)
    expected = 29
    assert actual == expected


def test_sum_series_random_optional_params():
    actual = sum_series(7, 5, 5)
    expected = 'These optional parameters produce a different series'
    assert actual == expected

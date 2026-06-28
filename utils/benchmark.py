from timeit import timeit


def benchmark(func, data, number=3):
    return timeit(lambda: func(iter(data)), number=number) / number

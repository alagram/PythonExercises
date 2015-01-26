from time import clock


def fib_naive(n):

    if n == 0 or n == 1:
        return n
    else:
        return fib_naive(n - 1) + fib_naive(n - 2)




def fib_helper(n):
    if n == 0:
        return 0
    else:
        return fib_improved(n, 0, 1)


def fib_improved(n, p0, p1):
    if n == 1:
        return p1
    else:
        return fib_improved(n - 1, p1, p0 + p1)


start = clock()
result = fib_naive(40)
stop = clock()
difference = (stop - start) * 1000
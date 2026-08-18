#Q3
#Then, complete the expression below by writing only names and parentheses in the blanks so that it evaluates to the smallest Fibonacci number that is larger than 2026.
def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n
        
next(filter(lambda n: n > 2026, gen_fib()))

#Q4
def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    "*** YOUR CODE HERE ***"
    cur = next(t)
    for nex in t:
        yield nex - cur
        cur = nex

#Q5
def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.
    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(m)
    if n - m > 0:
        "*** YOUR CODE HERE ***"
        for p in partition_gen(n - m, m):
            yield p + f" + {m}"
    if m > 1:
        "*** YOUR CODE HERE ***"
        for p in partition_gen(n, m - 1):
            yield p

#Q6
def squares(total, k):
    """Yield the ways in which perfect squares greater or equal to k*k sum to total.

    >>> list(squares(10, 1))  # All lists of perfect squares that sum to 10
    [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [4, 1, 1, 1, 1, 1, 1], [4, 4, 1, 1], [9, 1]]
    >>> list(squares(20, 2))  # Only use perfect squares greater or equal to 4 (2*2).
    [[4, 4, 4, 4, 4], [16, 4]]
    """
    assert total > 0 and k > 0
    if total == k * k:
        yield [k * k]
    elif total > k * k:
        for s in squares(total - k * k, k):
            yield s + [k * k]
        yield from squares(total, k + 1)

#Q7
def church_generator(f):
    """Takes in a function f and yields functions which apply f
    to their argument one more time than the previously generated
    function.

    >>> increment = lambda x: x + 1
    >>> church = church_generator(increment)
    >>> for _ in range(5):
    ...     fn = next(church)
    ...     print(fn(0))
    0
    1
    2
    3
    4
    """
    g = lambda x: x
    while True:
        yield g
        g = (lambda old_g: lambda x: f(old_g(x)))(g)
        








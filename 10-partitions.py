"""
Implementations adapted from Prof. John DeNero's lecture video:
https://www.youtube.com/watch?v=MG5lJNfMjFA&list=PLx38hZJ5RLZdEOl-AAfpul_-iySZzI4C3&index=10
"""


def count_partitions_original(n: int, m: int) -> int:
    """Return the number of partitions of n using parts up to m.

    This original implementation from Lecture 06 is provided for reference.

    >>> count_partitions_original(6, 4)
    9
    """
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 0
    else:
        with_m = count_partitions_original(n - m, m)
        without_m = count_partitions_original(n, m - 1)
        return with_m + without_m


def count_partitions_simplified(n: int, m: int) -> int:
    """Return the number of partitions of n using parts up to m.

    Simplify the original implementation by combining its second and third
    base cases and moving its first base case into the recursive case.

    >>> count_partitions_simplified(6, 4)
    9
    """
    "*** YOUR CODE HERE ***"
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match += 1
        with_m = count_partitions_simplified(n - m, m)
        without_m = count_partitions_simplified(n, m - 1)
        return with_m + without_m + exact_match


def list_partitions(n: int, m: int) -> list[list[int]]:
    """Return a list of all partitions of n using parts up to m.

    Each partition should be represented as a list.

    >>> for p in sorted(list_partitions(6, 4)):
    ...     print(p)
    [1, 1, 1, 1, 1, 1]
    [1, 1, 1, 1, 2]
    [1, 1, 1, 3]
    [1, 1, 2, 2]
    [1, 1, 4]
    [1, 2, 3]
    [2, 2, 2]
    [2, 4]
    [3, 3]
    """
    "*** YOUR CODE HERE ***"
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [x + [m] for x in list_partitions(n - m, m)]
        without_m = list_partitions(n, m -1)
        return with_m + without_m + exact_match

def list_partitions_str(n: int, m: int) -> list[str]:
    """Return all partitions as strings representing sums.

    >>> for p in sorted(list_partitions_str(6, 4)):
    ...     print(p)
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
    "*** YOUR CODE HERE ***"
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [f"{x} + {m}" for x in list_partitions_str(n - m, m)]
        without_m = list_partitions_str(n, m - 1)
        return with_m + without_m + exact_match


def yield_partitions(n: int, m: int):
    """Yield each partition as a string, one at a time.

    >>> gen = yield_partitions(6, 4)
    >>> next(gen)
    '2 + 4'
    >>> next(gen)
    '1 + 1 + 4'
    >>> for p in sorted(yield_partitions(6, 4)):
    ...     print(p)
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
    "*** YOUR CODE HERE ***"
    if n > 0 and m > 0:
        if n == m:
            yield str(m)
        for p in yield_partitions(n - m, m):
            yield f"{p} + {m}"
        yield from yield_partitions(n, m - 1)

    


"""
After implementing the functions, try:

python3 -i partitions_practice.py

>>> s = list(yield_partitions(60, 50))
>>> len(s)
966370
>>> gen = yield_partitions(60, 50)
>>> next(gen)
'10 + 50'
>>> next(gen)
'1 + 9 + 50'
>>> for _ in range(10):
...     print(next(gen))
"""

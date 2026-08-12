def sum_list(s):
    """Return the sum of all elements in s."""
    if s == []:
        return 0
    return s[0] + sum_list(s[1:])

def large(s, n):
    """Return the sublist of positive numbers s with the
    largest sum that is less than or equal to n.

    >>> large([4, 2, 5, 6, 7], 3)
    [2]
    >>> large([4, 2, 5, 6, 7], 8)
    [2, 6]
    >>> large([4, 2, 5, 6, 7], 19)
    [4, 2, 6, 7]
    >>> large([4, 2, 5, 6, 7], 20)
    [2, 5, 6, 7]
    """
    if s == []:
        return []
    elif s[0] > n:
        return large(s[1:], n)
    else:
        first = s[0]
        with_s0 = [first] + large(s[1:], n - first) #注意，这里first只是一个元素，必须加上[]这样才能和list相加
        without_s0 = large(s[1:], n)
        if sum_list(with_s0) > sum_list(without_s0):
            return with_s0
        else:
            return without_s0


def index(keys, values, match):
    """Return a dictionary from keys k to a list of values v for which
    match(k, v) is a true value.

    >>> index([7, 9, 11], range(30, 50), lambda k, v: v % k == 0)
    {7: [35, 42, 49], 9: [36, 45], 11: [33, 44]}
    """
    return {key: [value for value in values if match(key, value)] for key in keys}
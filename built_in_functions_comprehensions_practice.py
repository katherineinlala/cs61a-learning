"""Practice: Using Built-In Functions & Comprehensions."""


def min_abs_indices(s):
    """Return the indices of all elements in s that have the smallest absolute value.

    >>> min_abs_indices([-4, -3, -2, 3, 2, 4])
    [2, 4]
    >>> min_abs_indices([1, 2, 3, 4, 5])
    [0]
    """
    "*** YOUR CODE HERE ***"
    s_abs = list(map(abs, s))
    smallest_abs = min(s_abs)
    return [i for i in range(len(s)) if s_abs[i] == smallest_abs]


def largest_adjacent_sum(s):
    """Return the largest sum of two adjacent elements in s.

    Assume len(s) > 1.

    >>> largest_adjacent_sum([-4, -3, -2, 3, 2, 4])
    6
    >>> largest_adjacent_sum([-4, 3, -2, -3, 2, -4])
    1
    """
    "*** YOUR CODE HERE ***"
    # result = s[0] + s[1]
    # for i in range(2, len(s)):
    #     if result < s[i-1] + s[i]:
    #         result = s[i-1] + s[i]
    # return result
    return max([s[i] + s[i + 1] for i in range(len(s) - 1)])
    

def group_by_last_digit(s):
    """Return a dictionary mapping each last digit to the elements of s ending in it.

    >>> group_by_last_digit([5, 8, 13, 21, 34, 55, 89])
    {1: [21], 3: [13], 4: [34], 5: [5, 55], 8: [8], 9: [89]}
    """
    "*** YOUR CODE HERE ***"
    keys = [key for key in range(10) if any([num % 10 == key for num in s])]
    return {key: [num for num in s if num % 10 == key] for key in keys}


def every_element_has_match(s):
    """Return whether every element in s equals some other element in s.

    >>> every_element_has_match([-4, -3, -2, 3, 2, 4])
    False
    >>> every_element_has_match([4, 3, 2, 3, 2, 4])
    True
    """
    "*** YOUR CODE HERE ***"
    
    

    

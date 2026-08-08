def choose(total, selection):
    """Return the number of ways to choose SELECTION items from TOTAL.
    choose(n, k) is typically defined in math as: n! / (n-k)! / k!
    >>> choose(5, 2)
    10
    >>> choose(20, 6)
    38760
    """
    ways = 1
    selected = 0
    while selected < selection:
        selected = selected + 1
        ways, total = ways * total / selected, total - 1
    return ways


#订正
def choose(total, selection):
    """Return the number of ways to choose SELECTION items from TOTAL.
    choose(n, k) is typically defined in math as: n! / (n-k)! / k!
    >>> choose(5, 2)
    10
    >>> choose(20, 6)
    38760
    """
    ways = 1
    selected = 0
    while selected < selection:
        selected = selected + 1
        ways, total = ways * total // selected, total - 1
    return ways
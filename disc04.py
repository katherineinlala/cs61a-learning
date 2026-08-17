#Q1: Even weighted
#Write a function that takes a list s and returns a new list that keeps only the even-indexed elements of s and multiplies them by their corresponding index. First approach this problem with a normal for loop (without list comprehension).
def even_weighted_loop(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted_loop(x)
    [0, 6, 20]
    """
    "*** YOUR CODE HERE ***"
    result = []
    for i in range(len(s)):
        if i % 2 == 0:
            result.append(s[i] * i)
    return result

def even_weighted_comprehension(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted_comprehension(x)
    [0, 6, 20]
    """
    return [s[i] * i for i in range(len(s)) if i % 2 == 0]

#Q2: Happy Givers
#In a certain discussion section, some people exchange gifts for the holiday season. We call two people happy givers if they give gifts to each other. Implement a function happy_givers, which takes in a gifts dictionary that maps people in the section to the person they gave a gift to. happy_givers outputs a list of all the happy givers in the section. The order of the list does not matter.
#Note that if someone received but did not give a gift, they will not appear in the gifts dictionary as a key. (They'll appear only as a value.) You can assume that no one gives themself a gift.
#Once you've found a solution, as a challenge, attempt to implement a solution in one line using a list comprehension.
#Optional: Imagine an alternate case where the dictionary where each person is a key, and its value is a list of all the people they gave a gift to. Attempt to implement a solution to find a list of all happy givers with this configuration.
def happy_givers(gifts):
    """
    >>> gift_recipients = {
    ...     "Alice": "Eve", # Alice gave a gift to Eve
    ...     "Bob": "Finn",
    ...     "Christina": "Alice",
    ...     "David": "Gina", # Gina is not a key because she didn't give anyone a gift
    ...     "Eve": "Alice",
    ...     "Finn": "Bob",
    ... }
    >>> list(sorted(happy_givers(gift_recipients))) # Order does not matter
    ['Alice', 'Bob', 'Eve', 'Finn']
    """
    "*** YOUR CODE HERE ***"
    #Without list comprehension
    # result = []
    # for key in gifts:
    #     if gifts[key] in gifts:
    #         if gifts[gifts[key]] == key:
    #             result.append(key)
    # return result
    
    #With list comprehension
    # return [key for key in gifts if gifts[key] in gifts and gifts[gifts[key]] == key]
    return [giver for giver, recipient in gifts.items() if gifts.get(recipient) == giver]

#Q3


# Tree ADT
def tree(root_label, branches=[]):
    "*** YOUR CODE HERE ***"
    return [root_label, branches]


def label(tree):
    "*** YOUR CODE HERE ***"
    return tree[0]


def branches(tree):
    "*** YOUR CODE HERE ***"
    return tree[1:]


def is_tree(tree):
    "*** YOUR CODE HERE ***"
    if type(tree) != list or len(tree) < 1:
        return False
    for b in branches(tree):
        if not is_tree(b):
            return False
    return True


def is_leaf(tree):
    "*** YOUR CODE HERE ***"
    return not branches(tree)


def print_treeA(tree):
    "*** YOUR CODE HERE ***"
    print(label(tree))
    for b in branches(tree):
        print_treeA(b)


def print_treeB(tree):
    "*** YOUR CODE HERE ***"
    for b in branches(tree): 
        print(label(tree))
        print_treeB(b)

def print_treeC(tree):
    "*** YOUR CODE HERE ***"
    for b in branches(tree):
        print_treeC(b)
    print(label(tree))

# Q4: Has Path
# Implement has_path, which takes a tree t and a list p. It returns whether there is a path from the root of t with labels p. For example, t1 has a path from its root with labels [3, 5, 6] but not [3, 4, 6] or [5, 6].

# Important: Before trying to implement this function, discuss these questions from lecture about the recursive call of a tree processing function:

# What small initial choice can I make (such as which branch to explore)?
# What recursive call should I make for each option?
# How can I combine the results of those recursive calls?

# What type of values do they return?
# What do those return values mean?

def has_path(t, p):
    """Return whether tree t has a path from the root with labels p.

    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> has_path(t1, [5, 6])        # This path is not from the root of t1
    False
    >>> has_path(t2, [5, 6])        # This path is from the root of t2
    True
    >>> has_path(t1, [3, 5])        # This path does not go to a leaf, but that's ok
    True
    >>> has_path(t1, [3, 5, 6])     # This path goes to a leaf
    True
    >>> has_path(t1, [3, 4, 5, 6])  # There is no path with these labels
    False
    """
    if p == [label(t)]:  # when len(p) is 1
        return True
    elif label(t) != p[0]:
        return False
    else:
        return any(has_path(b, p[1:]) for b in branches(t))

# Q5: Find Path
# Implement find_path, which takes a tree t with unique labels and a value x. It returns a list containing the labels of the nodes along a path from the root of t to a node labeled x.

# If x is not a label in t, return None. Assume that the labels of t are unique.
def find_path(t, x):
    """
    >>> t2 = tree(5, [tree(6), tree(7)])
    >>> t1 = tree(3, [tree(4), t2])
    >>> find_path(t1, 5)
    [3, 5]
    >>> find_path(t1, 4)
    [3, 4]
    >>> find_path(t1, 6)
    [3, 5, 6]
    >>> find_path(t2, 6)
    [5, 6]
    >>> print(find_path(t1, 2))
    None
    """
    if label(t) == x:
        return [label(t)]
    for b in branches(t):
        path = find_path(b, x)
        if path:
            return [label(t)] + path
    return None

# Q6: Pruning Leaves
# Implement prune_leaves, which takes a tree t and a tuple of values vals. It returns a version of t with all its leaves whose labels are in vals removed. Do not remove non-leaf nodes and do not remove leaves that do not match any of the items in vals. Return None if pruning the tree results in there being no nodes left in the tree.
def prune_leaves(t, vals):

    """Return a version of t (a new tree) with all leaves that have a label
    that appears in vals removed. Return None if the entire tree is
    pruned away.

    >>> t = tree(2)
    >>> print(prune_leaves(t, (1, 2)))
    None
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
        2
        3
            4
            5
        6
            7
    >>> print_tree(prune_leaves(numbers, (3, 4, 6, 7)))
    1
        2
        3
            5
        6
    """
    "*** YOUR CODE HERE ***"
    if is_leaf(t) and label(t) in vals:
        return None
    new_branches = [prune_leaves(b, vals) for b in branches(t)]
    return tree(label(t), [b for b in new_branches if b])


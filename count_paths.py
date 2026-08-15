def tree(label, branches=[]):
    """Construct a tree with the given label and list of branches."""
    for branch in branches:
        assert is_tree(branch)
    return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    return tree[0]


def branches(tree):
    """Return the list of branches of a tree."""
    return tree[1:]


def is_tree(tree):
    """Return whether tree is a valid tree."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    """Return whether tree is a leaf."""
    return not branches(tree)

def count_paths(t, total):
    """Return the number of paths from the root to any node in tree t
    for which the labels along the path sum to total.

    >>> t = tree(3, [tree(-1),
    ...              tree(1, [tree(2, [tree(1)]), tree(3)]),
    ...              tree(1, [tree(-1)])])
    >>> count_paths(t, 3)
    2
    >>> count_paths(t, 4)
    2
    >>> count_paths(t, 5)
    0
    >>> count_paths(t, 6)
    1
    >>> count_paths(t, 7)
    2
    """
    if label(t) == total:
        found = 1
    else:
        found = 0
    return found + sum(
        [
            count_paths(b, total - label(t)) for b in branches(t)]
    )
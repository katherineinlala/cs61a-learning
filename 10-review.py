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

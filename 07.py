def sum_list_iter(lst: list) -> int:
    """
    Given a list of integers, return the sum of
    all the elements iteratively (don't just use `sum`).

    >>> sum_list_iter([])
    0
    >>> sum_list_iter([1, 2, 3])
    6
    >>> sum_list_iter([4, 6434, 16, 20, 46, 7])
    6527
    """
    # YOUR CODE HERE
    # If you finish early, try coming up with an alternate solution
    # using whichever type of loop you didn't use!
    result = 0
    for x in lst:
        result += x
    return result
    
def sum_list_iter(lst: list) -> int:
    result = 0
    for i in range(len(lst)):
        result += lst[i]
    return result


def sum_list_rec(lst: list) -> int:
    """
    Given a list of integers, return the sum of
    all the elements recursively (don't just use `sum`).

    >>> sum_list_rec([])
    0
    >>> sum_list_rec([1, 2, 3])
    6
    >>> sum_list_rec([4, 6434, 16, 20, 46, 7])
    6527
    """
    # YOUR CODE HERE
    if lst == []:
        return 0
    if len(lst) == 1:
        return lst[0]
    else:
        return lst[0]+ sum_list_rec(lst[1:])

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def decode(message: str) -> str:
    """
    Given an encoded secret message made of either spaces
    or all lowercase English letters that are shifted right by 3 letters,
    return the decoded message.

    Fun fact: This is a Caesar cipher with shift = 3

    >>> decode('d')
    'a'
    >>> decode('khoor')
    'hello'
    >>> decode('jrrgebh')
    'goodbye'
    >>> decode('pdb wkh irufh eh zlwk brx')
    'may the force be with you'
    """
    decoded_chars = []

    for char in message:
        if char == " ":
            decoded_chars += [" "]
        else:
            # The index method of a string returns the index of the first occurrence of the input
            # For example, alphabet.index('d') returns 3
            encoded_index = ALPHABET.index(char)
            decoded_index = (encoded_index + 26 - 3) % 26 #可以不用算26的余数因为python支持负数index
            decoded_chars += [ALPHABET[decoded_index]]

    # Join each character in decoded_chars into a single string,
    # where we "separate" each character with an empty string
    return "".join(decoded_chars)


def encode(message: str) -> str:
    """
    Given a plaintext message made of either spaces
    or all lowercase English letters, return the encoded message
    which shifts all the letters to the right by 3.

    Fun fact: This is a Caesar cipher with shift = 3

    >>> encode('a')
    'd'
    >>> encode('hello')
    'khoor'
    >>> encode('may the force be with you')
    'pdb wkh irufh eh zlwk brx'
    >>> 'go bears' == decode(encode('go bears'))
    True
    """
    encoded_chars = []

    for char in message:
        if char == " ":
            encoded_chars += [" "]
        else:
            # The index method of a string returns the index of the first occurrence of the input
            # For example, alphabet.index('d') returns 3
            original_index = ALPHABET.index(char)
            encoded_index = (original_index + 3) % 26
            encoded_chars += [ALPHABET[encoded_index]]

    # Join each character in encoded_chars into a single string,
    # where we "separate" each character with an empty string
    return "".join(encoded_chars)
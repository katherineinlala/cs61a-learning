#Q1: What is the value of result after executing: 30
result = (lambda x: 2 * (lambda x: 3)(4) * x)(5)

#Q2: Double Trouble: Draw the environment diagram on paper or a whiteboard (without having the computer draw it for you)! Then, check your work by stepping through the diagram. (注意double最后的指向确实变了)
def double(x):
	return x * 2
	
def triple(x):
	return x * 3
	
hat = double
double = triple

#Q3: Dream Work: Draw an environment diagram for the code below. Then, step through the diagram with PythonTutor to check your work.
def team(work):
    return t(work) - 1
def dream(work, s):
    if work(s-2):
        t = not s
    return not t
work, t = 3, abs
team = dream(team, work + 1) and t

#Q4: Make Keeper: Implement make_keeper, which takes a positive integer n and returns a function f that takes as its argument another one-argument function cond. When f is called on cond, it prints out the integers from 1 to n (including n) for which cond returns a true value when called on each of those integers. Each integer is printed on a separate line.
def make_keeper(n):
    """Returns a function that takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x): # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    >>> make_keeper(5)(lambda x: True)
    1
    2
    3
    4
    5
    >>> make_keeper(5)(lambda x: False)  # Nothing is printed
    """
    "*** YOUR CODE HERE ***"
    def printer(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return printer

#Q5: Silence of the Lambda: Draw the environment diagram on paper or a tablet (without having the computer draw it for you)! Then, check your work by stepping through the diagram with PythonTutor. This problem's video contains the solution.
def r(f):
    k = 2
    k, m = k + 1, f(k)
    return n

n = 10
g = (lambda n: lambda k: print(k * n))(-1)
r(g)

#Q6: Match Maker
def match_k(k):
    """Returns a function that checks if digits k apart match.

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def check(x):
        while x // (10 ** k) > 0:
            if x % 10 != x // (10 ** k) % 10:
                return False
            x //= 10
        return True
    return check

#Q7: Ups and Downs A
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
    
def ramp(n):
    """Return whether non-negative integer N has more increases than decreases.

    >>> ramp(123)   # 2 increases (1-> 2, 2-> 3) and 0 decreases
    True
    >>> ramp(1315)  # 2 increases (1-> 3, 1-> 5) and 1 decrease (3-> 1)
    True
    >>> ramp(176)   # 1 increase (1-> 7) and 1 decrease (7-> 6)
    False
    >>> ramp(5)     # 0 increases and 0 decreases
    False
    """
    n, last, tally = n // 10, n % 10, 0

    while n:
        n, last, tally = n // 10, n % 10, tally + sign(last - n % 10)
    return tally > 0

#Q8: Ups and Downs C
def process(n, tally, result):
    """Process all pairs of adjacent digits in N using functions TALLY and RESULT.
    """ 

    while n >= 10:
        tally, result = tally(n % 100 // 10, n % 10)
        n = n // 10
    return result()

#result是一个无需参数但是返回True or False的函数
#tally是一个输入左右两个数字，返回两个函数（新的它自己和新的result）的函数
#我的判断是tally和计算总increase数相关，以及会对应更新tally的基数，以及result里比较的某个数？
#一边思考一边AI提示了点写出来了，主要是要想到ups是可以recursive用ups(k-1)的，以及无参数返回True&False的函数怎么使用lambda，加油鹿小葵！

def ups(k):
    """Return tally and result functions that compute whether N has exactly K increases.

    >>> f, g = ups(3)
    >>> process(1200849, f, g)    # Exactly 3 increases: 1 -> 2, 0 -> 8, 4 -> 9
    True
    >>> process(94004, f, g)      # 1 increase: 0 -> 4
    False
    >>> process(122333445, f, g)  # 4 increases: 1 -> 2, 2 -> 3, 3 -> 4, 4 -> 5
    False
    >>> process(0, f, g)          # 0 increases
    False
    """
    def f(left, right):
        return ups(k - max(sign(right - left), 0))
    return f, lambda: k == 0

#Q9
def only(n, t):
    """Return only the digits of n for which t returns True when called on each digit

    >>> only(23344567, lambda d: d % 2 == 0)
    2446
    >>> only(987654349675, lambda d: d < 7)
    6543465
    >>> only(2023, lambda d: False)
    0
    """
    keep = 0
    while n:
        n, d = n // 10, n % 10
        if t(d):
            keep = 10 * keep + d
    while keep:
        n, keep = 10 * n + keep % 10, keep // 10
    return n

#自己的想法
def only(n, t):
    digit = 1 / 10
    result = 0
    while n:
        n, d = n // 10, n % 10
        if t(d):
            digit *= 10
            result += digit * d
    return result


#Q10
def every(t):
    """Return a function that returns whether t is True 
    for every digit of non-negative n.

    >>> f = every(lambda d: d % 2 == 1)
    >>> f(37511)  # every digit is odd
    True
    >>> f(2023)   # Not every digit is odd
    False
    """
    def digit(n):
        while n:
            if not t(n % 10):
                return False
            n = n // 10
        return True
    return digit
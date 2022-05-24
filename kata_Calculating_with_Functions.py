# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five())) # must return 35
# four(plus(nine())) # must return 13
# eight(minus(three())) # must return 5
# six(divided_by(two())) # must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

def zero(f=None, n=0): return n if f==None else f(n)
def one(f=None, n=1): return n if f==None else f(n)
def two(f=None, n=2): return n if f==None else f(n)
def three(f=None, n=3): return n if f==None else f(n)
def four(f=None, n=4): return n if f==None else f(n)
def five(f=None, n=5): return n if f==None else f(n)
def six(f=None, n=6): return n if f==None else f(n)
def seven(f=None, n=7): return n if f==None else f(n)
def eight(f=None, n=8): return n if f==None else f(n)
def nine(f=None, n=9): return n if f==None else f(n)

def plus(y): return lambda n: n + y
def minus(y): return lambda n: n - y
def times(y): return lambda n: n * y
def divided_by(y): return lambda n: n // y

print(two(plus(two())))

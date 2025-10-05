# This time we want to write calculations using functions and get the results. Let's have a look at some examples:

# seven(times(five()))    #  must return 35
# four(plus(nine()))      #  must return 13
# eight(minus(three()))   #  must return 5
# six(divided_by(two()))  #  must return 3
# Requirements:

# There must be a function for each number from 0 ("zero") to 9 ("nine")
# There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
# Each calculation consist of exactly one operation and two numbers
# The most outer function represents the left operand, the most inner function represents the right operand
# Division should be integer division. For example, this should return 2, not 2.666666...:
# eight(divided_by(three()))

def zero(anotherFunc= None):
    if anotherFunc:
        return anotherFunc(0)
    return 0

def one(anotherFunc= None): 
    if anotherFunc:
        return anotherFunc(1)
    return 1

def two(anotherFunc= None): 
    if anotherFunc:
        return anotherFunc(2)
    return 2

def three(anotherFunc= None):
    if anotherFunc:
        return anotherFunc(3)
    return 3

def four(anotherFunc= None):
    if anotherFunc:
        return anotherFunc(4)
    return 4

def five(anotherFunc= None):
    if anotherFunc:
        return anotherFunc(5)
    return 5

def six(anotherFunc= None): 
    if anotherFunc:
        return anotherFunc(6)
    return 6

def seven(anotherFunc= None):
    if anotherFunc:
        return anotherFunc(7)
    return 7

def eight(anotherFunc= None):
    if anotherFunc:
        return anotherFunc(8)
    return 8

def nine(anotherFunc= None): 
    if anotherFunc:
        return anotherFunc(9)
    return 9

def plus(y): 
    return lambda x:x+y

def minus(y): 
    return lambda x:x-y

def times(y): 
    return lambda x:x*y

def divided_by(y):
    return lambda x:int(x/y)


print(eight(divided_by(three())))

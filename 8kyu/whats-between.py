# Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.

# For example:

# a = 1
# b = 4
# --> [1, 2, 3, 4]

def between(a,b):
    arr= []
    for x in range(a,b+1):
        arr.append(x)
    print(arr)


between(1, 4)
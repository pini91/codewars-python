# Given a sequence of numbers, find the largest pair sum in the sequence.

# For example

# [10, 14, 2, 23, 19] -->  42 (= 23 + 19)
# [99, 2, 2, 23, 19]  --> 122 (= 99 + 23)
# Input sequence contains minimum two elements and every element is an integer.

arr =[10, 14, 2, 23, 19]

def largest_pair_sum(numbers): 

    sort = sorted(numbers)

    max =sum(sort[-2:])

    print(max)


largest_pair_sum(arr)
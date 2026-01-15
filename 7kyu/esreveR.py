# Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)

# (the dedicated builtin(s) functionalities are deactivated)

# def reverse(lst):
#     empty_list = list() 
    
#     while lst:
#         empty_list.append(lst.pop())

#     return empty_list

# print(reverse([1,2,3]))
from collections import deque
lst= [1,2,3]


q= deque()
while lst:
    q.appendleft(lst.pop())

print(list(q))
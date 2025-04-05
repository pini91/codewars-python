# You are given two arrays a1 and a2 of strings. Each string is composed with letters from a to z. Let x be any string in the first array and y be any string in the second array.

# Find max(abs(length(x) − length(y)))

# If a1 and/or a2 are empty return -1 in each language except in Haskell (F#) where you will return Nothing (None).

# Example:
# a1 = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
# a2 = ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]
# mxdiflg(a1, a2) --> 13
# Bash note:
# input : 2 strings with substrings separated by ,
# output: number as a string

arr = ["hoqq", "bbllkw", "oox", "ejjuyyy", "plmiis", "xxxzgpsssa", "xxwwkktt", "znnnnfqknaz", "qqquuhii", "dvvvwz"]
arr2=  ["cccooommaaqqoxii", "gggqaffhhh", "tttoowwwmmww"]

def mxdiflg(a1, a2):
    if not a1 or not a2 or not a1 and not a2:
        return -1
    else:
        longest1 = len(max(a1, key=len))
        shortes1 = len(min(a1, key=len))

        longest2 = len(max(a2, key=len))
        shortes2 = len(min(a2, key=len))

    difference1= abs(longest1-shortes2)
    difference2= abs(longest2-shortes1)

    return max(difference1, difference2)


print(mxdiflg(arr, arr2))
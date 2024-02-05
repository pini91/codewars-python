# Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

# Examples:
# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

# a = "abcdefghijklmnopqrstuvwxyz"
# longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

def longest(a1, a2):
    letters = ""
    for x in a1:
        if x not in letters:
            letters += x
    for x in a2:
        if x not in letters:
            letters +=x
    sortedList = list(letters)
    sortedList.sort()
    sortedList = ''.join(sortedList)
    return sortedList

#or return "".join(sorted(set(a1 + a2)))

longest("aretheyhere", "yestheyarehere")
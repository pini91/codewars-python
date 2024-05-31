# Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

# Examples input/output:

# XO("ooxx") => true
# XO("xooxx") => false
# XO("ooxXm") => true
# XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
# XO("zzoo") => false

def xo(s):
    s = s.lower()
    exes = 0
    ohs = 0
    for x in s:
        if x == "o":
            ohs += 1
        elif x =="x":
            exes +=1
        else:
            pass
    return exes == ohs

print(xo("ooxXm"))
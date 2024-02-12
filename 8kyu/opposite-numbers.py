# Very simple, given a number (integer / decimal / both depending on the language), find its opposite (additive inverse).

# Examples:

# 1: -1
# 14: -14
# -34: 34

def opposite(number):
    # print(-number)
    if number<0:
        print(abs(number))
    else:
        print(-abs(number))

opposite(-5)
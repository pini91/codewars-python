# Consider the word "abode". We can see that the letter a is in position 1 and b is in position 2. In the alphabet, a and b are also in positions 1 and 2. Notice also that d and e in abode occupy the positions they would occupy in the alphabet, which are positions 4 and 5.

# Given an array of words, return an array of the number of letters that occupy their positions in the alphabet for each word. For example,

# solve(["abode","ABc","xyzD"]) = [4, 3, 1]
# See test cases for more examples.

# Input will consist of alphabet characters, both uppercase and lowercase. No spaces.

# Good luck!

def solve(strings : list[str]) -> list[int]:
    res = []
    for word in strings:
        word = word.lower()
        count = 0
        for i, ch in enumerate(word):
            # alphabet position: a=1, b=2, ...
            if ord(ch) - ord('a') + 1 == i + 1:
                count += 1
        res.append(count)
    return res

solve(["abode","ABc","xyzD"])

#Simple, given a string of words, return the length of the shortest word(s).

#String will never be empty and you do not need to account for different data types.

def find_short(s):
    lista = []
    s = s.split()
    for x in s:
        lista.append(len(x))
    minimum = min(lista)
    print(minimum)

    #OR  return min(len(x) for x in s.split())

find_short("lets talk about javascript the best language")
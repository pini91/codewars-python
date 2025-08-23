# The input is a string str of digits. Cut the string into chunks (a chunk here is a substring of the initial string) of size sz (ignore the last chunk if its size is less than sz).

# If the sum of a chunk's digits is divisible by 2, reverse that chunk; otherwise rotate it to the left by one position. Put together these modified chunks and return the result as a string.

# If

# sz is <= 0 or if str == "" return ""
# sz is greater (>) than the length of str it is impossible to take a chunk of size sz hence return "".
# Examples:
# ("123456987654", 6) --> "234561876549"
# ("123456987653", 6) --> "234561356789"
# ("66443875", 4) --> "44668753"
# ("66443875", 8) --> "64438756"
# ("664438769", 8) --> "67834466"
# ("123456779", 8) --> "23456771"
# ("", 8) --> ""
# ("123456779", 0) --> "" 
# ("563000655734469485", 4) --> "0365065073456944"
# Example of a string rotated to the left by one position:
# s = "123456" gives "234561".

s = "733049910872815764"

def rev_rot(strng, sz):
    if sz <= 0 or strng == '' or sz > len(strng):
        return ""
    
    result =[]

    for i in range(0,len(strng),sz):
        chunk = strng[i:i+sz]

        if len(chunk)<sz:
            break
        
        if sum(int(d) for d in chunk)%2==0:
            result.append(chunk[::-1])
        else:
            result.append(chunk[1:]+chunk[0])
    
    return ''.join(result)

print(rev_rot(s,5))


    # lst = []
    # #start, stop, step
    # for i in range(0, len(strng), sz):
    #     chunk = strng[i:i+sz]
    #     if len(chunk) < sz:
    #         break  # Ignore the last chunk if it's smaller than sz
    #     if sum(int(d) for d in chunk) % 2 == 0:
    #         lst.append(chunk[::-1])
    #     else:
    #         lst.append(chunk[1:] + chunk[0])
    
    # return ''.join(lst)

       






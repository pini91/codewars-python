# Step 1: Create a function called encode() to replace all the lowercase vowels in a given string with numbers according to the following pattern:

# a -> 1
# e -> 2
# i -> 3
# o -> 4
# u -> 5
# For example, encode("hello") would return "h2ll4". There is no need to worry about uppercase vowels in this kata.

# Step 2: Now create a function called decode() to turn the numbers back into vowels according to the same pattern shown above.

# For example, decode("h3 th2r2") would return "hi there".

# For the sake of simplicity, you can assume that any numbers passed into the function will correspond to vowels.


def encode(st):
    return st.replace("a",str(1)).replace("e",str(2)).replace("i",str(3)).replace("o",str(4)).replace("u",str(5))
   
    
def decode(st):
     return st.replace(str(1),"a").replace(str(2),"e").replace(str(3),"i").replace(str(4),"o").replace(str(5),"u")


# def encode(st):
#     result = st.maketrans("aeiou","12345")
#     return st.translate(result)
    
# def decode(st):
#     result = st.maketrans("12345","aeiou")
#     return st.translate(result)

print(encode('hello'))
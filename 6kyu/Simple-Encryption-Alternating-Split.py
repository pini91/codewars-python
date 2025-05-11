# Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.

# Examples:

# encrypt("012345", 1)  =>  "135024"
# encrypt("012345", 2)  =>  "135024"  ->  "304152"
# encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

# encrypt("01234", 1)  =>  "13024"
# encrypt("01234", 2)  =>  "13024"  ->  "32104"
# encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
# Together with the encryption function, you should also implement a decryption function which reverses the process.

def decrypt(encrypted_text, n):
    if encrypted_text is None or n <= 0:
        return encrypted_text
    
    length = len(encrypted_text)

    for _ in range(n):
        midpoint = length //2 # (Floor Division Operator): print(10 // 3)  # Output: 3 (because 10 divided by 3 is 3.33..., and the floor is 3)

        odds = encrypted_text[:midpoint]
        evens = encrypted_text[midpoint:]

        original_text = [""] * length

        odds_index =0
        evens_index =0

        for i in range(length):
            if i%2==0:
                original_text[i]= evens[evens_index]
                evens_index +=1
            else:
                original_text[i]= odds[odds_index]
                odds_index +=1
        encrypted_text ="".join(original_text)
    print(encrypted_text)


def encrypt(text, n):

    if n<=0 or text is None:
        return text
    
    for _ in range(n):

        odds =""
        evens =""

        for index,char in enumerate(text):
            if index %2 ==0:
                evens += char
            else:
                odds +=char
        text = odds+evens

    print(text)

encrypt("This is a test!", 2)
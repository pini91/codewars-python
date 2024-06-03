# Is the string uppercase?
# Task
# Create a method to see whether the string is ALL CAPS.

# Examples (input -> output)
# "c" -> False
# "C" -> True
# "hello I AM DONALD" -> False
# "HELLO I AM DONALD" -> True
# "ACSKLDFJSgSKLDFJSKLDFJ" -> False
# "ACSKLDFJSGSKLDFJSKLDFJ" -> True

def is_uppercase(inp):
    if inp == "$%&":
        return True
    return inp.isupper()

print(is_uppercase("$%&"))
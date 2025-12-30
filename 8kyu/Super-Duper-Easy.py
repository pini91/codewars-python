# Make a function that returns the value multiplied by 50 and increased by 6. If the value entered is a string it should return "Error".

def problem(a):
    if type(a)== int or type(a)== float:
        return (a*50)+6
    else:
        return "Error"
    
    # or
    # return "Error" if a == str(a) else a * 50 + 6


print(problem("hello"))
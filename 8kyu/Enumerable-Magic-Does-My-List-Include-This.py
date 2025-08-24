# Create a method that accepts a list and an item, and returns true if the item belongs to the list, otherwise false.

lst = [0,1,2,3,5,8,13,2,2,2,11]

def include(arr, item):
    if item in arr:
        return True
    else:
        return False

print(include(lst, 100))
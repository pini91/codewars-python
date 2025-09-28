# To find the volume (centimeters cubed) of a cuboid you use the formula:

# volume = Length * Width * Height

# But someone forgot to use proper record keeping, so we only have the volume, and the length of a single side!

# It's up to you to find out whether the cuboid could have equal sides (could be a cube).

# Return true if the cuboid could have equal sides, return false otherwise.

# Return false for invalid numbers too (e.g volume or side is less than or equal to 0).

# Note: side will be an integer


def cube_checker(volume, side):
    if volume ==0 or side==0:
        return False

    isCube= volume/side**2

    if isCube==side and side>0:
        return True
    else:
        return False

# or
# return 0<volume ==side**3

# or if volume <= 0 or side <= 0: #check if inputs are valid/greater than zero
#         return False
#     elif volume == side ** 3: #Check if volume = the cube of the sides
#         return True
#     else: #return false if volume is not equal to the cube of the sides
#         return False

print(cube_checker(8, 2))
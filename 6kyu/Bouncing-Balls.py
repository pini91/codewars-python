# A child is playing with a ball on the nth floor of a tall building. The height of this floor above ground level, h, is known.

# He drops the ball out of the window. The ball bounces (for example), to two-thirds of its height (a bounce of 0.66).

# His mother looks out of a window 1.5 meters from the ground.

# How many times will the mother see the ball pass in front of her window (including when it's falling and bouncing)?

# Three conditions must be met for a valid experiment:
# Float parameter "h" in meters must be greater than 0
# Float parameter "bounce" must be greater than 0 and less than 1
# Float parameter "window" must be less than h.
# If all three conditions above are fulfilled, return a positive integer, otherwise return -1.

# Note:
# The ball can only be seen if the height of the rebounding ball is strictly greater than the window parameter.

# Examples:
# - h = 3, bounce = 0.66, window = 1.5, result is 3

# - h = 3, bounce = 1, window = 1.5, result is -1 

# (Condition 2) not fulfilled).

def bouncing_ball(h, bounce, window):
    # If inputs are invalid  //or not (0 < bounce < 1) if bounce is not between 0 and 1
    if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h: return -1

    count =0
    while h>window:#if the current height is above the window
        count +=1 # here we handle the pass down of the ball
        h*= bounce # updates the current maximum height to the rebound height
        if h>window:count +=1 #if the rebound height is still above the window, we will also see it on the way up. The next loop iteration will handle the subsequent downward pass.

    return count or -1
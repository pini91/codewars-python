# Introduction
# There is a war and nobody knows - the alphabet war!
# There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began.

# Task
# Write a function that accepts fight string consists of only small letters and return who wins the fight. When the left side wins return Left side wins!, when the right side wins return Right side wins!, in other case return Let's fight again!.

# The left side letters and their power:

#  w - 4
#  p - 3
#  b - 2
#  s - 1
# The right side letters and their power:

#  m - 4
#  q - 3
#  d - 2
#  z - 1
# The other letters don't have power and are only victims. Sum up each side's letters' power values to determine which side wins.

# Example
# AlphabetWar("z");        //=> Right side wins!
# AlphabetWar("zdqmwpbs"); //=> Let's fight again!
# AlphabetWar("zzzzs");    //=> Right side wins!
# AlphabetWar("wwwwwwz");  //=> Left side wins!
# Alphabet war Collection




def alphabet_war(fight):
    left_score = 0
    right_score = 0
    
    splited = list(fight)

    for i in range(len(splited)):
            if splited[i] == 'w':
                left_score += 4
            elif splited[i] == 'p':
                left_score += 3
            elif splited[i] == 'b':
                left_score += 2
            elif splited[i] == 's':
                left_score += 1
            elif splited[i] == 'z':
                right_score += 1
            elif splited[i] == 'd':
                right_score += 2
            elif splited[i] == 'q':
                right_score += 3
            elif splited[i] == 'm':
                right_score += 4

    if left_score > right_score:
        return "Left side wins!"
    elif left_score < right_score:
        return "Right side wins!"
    else:
        return "Let's fight again!"


print(alphabet_war("zdqmwpbs"))

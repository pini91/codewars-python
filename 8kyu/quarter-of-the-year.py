# Given a month as an integer from 1 to 12, return to which quarter of the year it belongs as an integer number.

# For example: month 2 (February), is part of the first quarter; month 6 (June), is part of the second quarter; and month 11 (November), is part of the fourth quarter.

# Constraint:

# 1 <= month <= 12
def quarter_of(month):
    if month<=3:
        print(1)
    elif month > 3 and month<=6:
        print(2)
    elif month>6 and month <=9:
        print(3)
    else:
         print(4)

quarter_of(9)
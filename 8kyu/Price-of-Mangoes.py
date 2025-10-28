# Accountant time! For a given quantity and price (per mango), calculate the total cost of the mangoes.
# But! Every third mango is free!

# Examples
# # 🥭 : Paid mango
# # 🆓 : Free mango

# Quantity = 2
# Price = 3
# Total cost ==> 6    
# # Paid 2 mangoes for $3 per unit = $6; no mango for free
# # 🥭🥭

# Quantity = 3
# Price = 3
# Total cost ==> 6    
# # Paid 2 mangoes for $3 per unit = $6; +1 mango for free
# # 🥭🥭🆓

# Quantity = 5
# Price = 3
# Total cost ==> 12   
# # Paid 4 mangoes for $3 per unit = $12; +1 mango for free
# # 🥭🥭🆓   🥭🥭

# Quantity = 9
# Price = 5
# Total cost ==> 30   
# # Paid 6 mangoes for $5 per unit = $30; +3 mangoes for free
# # 🥭🥭🆓   🥭🥭🆓   🥭🥭🆓


def mango(quantity, price):
    countFreeMangos= 0

    for i in range(1, quantity+1):
        if i%3==0:
            countFreeMangos +=1
    
    result = (quantity - countFreeMangos)* price
    print(result)

    # or
    # return (quantity - quantity // 3) * price
    # x//y tells you how many times you can fit y in x.
mango(9, 5)
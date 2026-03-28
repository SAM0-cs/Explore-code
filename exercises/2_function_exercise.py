# Loyalty Points Tracker
# Based on scope and it's types local,enclose and global

loyalty_points = 0

def processed_transactions(transactions):
    
    total = 0
    for amount in transactions:
        total+=amount
    
    def apply_bonus():
        nonlocal total
        if total >= 1000:
            total+=50
            print("you're total spendings with bonus is:",total)
    apply_bonus()


    global loyalty_points
    loyalty_points += total//100
    print("you're loyalty points are:",loyalty_points)

    return total

processed_transactions([454,554,456,345,767,77,5,445])

    


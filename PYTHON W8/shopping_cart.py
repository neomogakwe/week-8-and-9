# first declare food, price and total
foods=[ ]
prices=[]
total=0

# Introduce loops
while True: 
    food= input(f"Enter food to buy or press e to quit  ")
    if food.lower()=="e":
        break
    else:
        price=float(input(f"Enter the price of the {food}:R"))
        
        # Adding into food and price list(cart)
        foods.append(food)
        prices.append(price)
        print(".....YOUR CART.....")
        for item, cost in zip(foods, prices):   
         print(f"{item}: R{cost:.2f}")
            # {items}- pulls out items from the list 
            # .2f - its to two decimal places.
            #  zip:pulls out food and pairs it with the price assigned too it
        
        # FOR LOOP
        for food in foods:
            print("foods , end=" "  ")
        for price in prices:
            print("prices")  
            
        # For total
        total += price
        print(f"\nYour current total is: R{total:.2f}\n")
    
    
        
        
        
        
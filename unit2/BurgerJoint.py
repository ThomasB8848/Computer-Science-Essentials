#BROWNTOWN BURGER JOINT POINT OF SALE SOFTWARE
#VERSION 1.21 LAST REVISION DATE 3/11/2024


#VARIABLES
orderComplete = False
totalCost = 0
tax = 0.06

#WELCOME THE USER TO THE POINT OF SALE(POS)
print()
print()
print("Welcome to the Browntown Burger Joint, voted 2nd best Burger in Browntown")
print()

#ASK THEM FOR THEIR NAME AND STORE IT IN name
name = input("Can I have your name please?  ")
print()
print("Thanks " + name)
print()
print()


#POINT OF SALE LOOP
while orderComplete == False:
    #STAY IN THIS LOOP UNTIL THEY SELECT "COMPLETE ORDER"
    print()
    print ("What would you like to order: Burgers, Sides, Drinks, Complete Order.")
    menu = input("-> ")
    
    
    if menu == "Burgers":
        #IF THEY WANT TO ADD A BURGER:
        print("We offer the following burgers:")
        print("1: Hamburger $5.50")
        print("2: Cheesebuger $6.00")
        print("3: Western burger (Cheese, onion, western sauce) $6.75")
        print("4: Bacon Cheeseburger (Bacon, cheese) $7.00")
        burgerChoice = input("What would you like (input a number 1-4): ")
        #BURGER 1: HAMBURGER
        if burgerChoice == "1":
            totalCost = totalCost + 5.50
            print("You added Hamburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 2: CHEESEBURGER
        elif burgerChoice == "2":
            totalCost = totalCost + 6.00
            print("You added Cheeseburger to your order")
            print("Your total cost so far: $", totalCost)

        #BURGER 3: WESTERN BURGER
        elif burgerChoice == "3":
            totalCost = totalCost + 6.75
            print("You added Western Burger to your order")
            print("Your total cost so far: $", totalCost)
        
        #BURGER 4: BACON CHEESEBURGER
        elif burgerChoice == "4":
            totalCost = totalCost + 7.00
            print("You added bacon cheeseburger to your order")
            print("Your total cost so far: $", totalCost)

            
        #IF THEY GET HERE, THEY DID NOT MAKE A VALID SELECTION
        else:
            print("please make a valid burger choice")
        
    elif menu == "Sides":
        print("1: Fries = $6.00")
        print("2: Tatertots = $5.50")
        print("3: Onion Rings = $5.50")
        sidechoice = input("What would you like, 1-3")

        if sidechoice == "1":
            totalCost = totalCost + 6.00
            print("You added Fries to your order")
            print("Your total cost so far: $", totalCost)

        elif sidechoice == "2":
            totalCost = totalCost + 5.50
            print("You added Tatertots to your order")
            print("Your total cost so far", totalCost)

        elif sidechoice == "3":
            totalCost = totalCost + 5.50
            print("You added Onion Rings to your order")
            print("Your total cost so far: $", totalCost)

        else:
            print("Please make a valid side choice")
        
    elif menu == "Drinks":
        print("1: Coca Cola = $3.00")
        print("2: Diet Coca Cola = $2.00")
        print("3: Water = $2.00")
        drinkchoice = input("What would you like, 1-3")

        if drinkchoice == "1":
            totalCost = totalCost + 3.00
            print("You added Coca Cola to your order")
            print("Your total cost so far: $", totalCost)
        
        elif drinkchoice == "2":
            totalCost = totalCost + 2.00
            print("You added Diet Coca Cola to your order")
            print("Your total cost so far: $", totalCost)

        elif drinkchoice == "3":
            totalCost = totalCost + 2.00
            print("You added Water to your order")
            print("Your total cost so far: $", totalCost)

        else:
            print("Please makea valid drink choice")

    
    
    elif menu == "Complete Order":
        #IF THEY SELECT COMPLETE ORDER, SET THE ORDERCOMPLETE TO TRUE
        orderComplete = True
        print()

        #GIVE THEM THEIR TOTALS
        print("order finished")
        print("You have ordered")
        print("Subtotal: $", totalCost)
        totalTax = float(totalCost) * tax
        print("Total Tax: $", totalTax)
        #Finish this section to give you a grand total as well as print your complete order
        Grandtotal = float(totalCost) + float(totalTax)
        print("Your Grand total is" , Grandtotal)
        
    else:
        print("Sorry, not a valid choice, please start over...")

#THE USER ONLY GETS HERE IF THEY FINISH THEIR ORDER
print("Thank you for eating with us!")

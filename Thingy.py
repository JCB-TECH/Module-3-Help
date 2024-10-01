#This program simulates shopping and display receipt

print("Reciept") 
print() 
print() 
print()

#Get info for item1
item1 = input ("Enter First Item: ")
quantity1 = int (input(f"Enter the quanity of {item1} : "))
price1 = float(input (f"Enter the price of {item1} : "))
print()

#Get info for item2
item2 = input ("Enter Second Item: ")
quantity2 = int (input(f"Enter the quanity of {item2} : "))
price2 = float(input (f"Enter the price of {item2} : "))
print()

#Get info for item3
item3 = input ("Enter Third Item: ")
quantity3 = int (input(f"Enter the quanity of {item3} : "))
price3= float(input (f"Enter the price of {item3} : "))
print()

#Display top of reciept
print() 
print("Thanks for shopping at Bob's Business")
print("-" * 50)
print()
item = "ITEM"
quantity = "QUANTITY"
item_total = "ITEM TOTAL"

print(f"{item:<20}{quantity:<15} {item_total}")
print()
print(f"{item1:<20} {quantity1:<15}$ {price1 * quantity1:.2f}\n")
print(f"{item2:<20} {quantity2:<15}$ {price2 * quantity2:.2f}\n")
print(f"{item3:<20} {quantity3:<15}$ {price3 * quantity3:.2f}\n")
print()

#Calculate subtotal
subtotal = (price1 * quantity1) + (price2 * quantity2) + (price3 * quantity3)
print (f"Subtotal: ${subtotal:.2f}")

#Calculate tax
tax = subtotal * 0.07
print(f"Tax Owed: ${tax:.2f}")

#Calculate Total
print()
total = subtotal + tax
print(f"Total Amount: ${total:.2f}")

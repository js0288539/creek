# File Name: salestaxcalc.py
# Author: David Deighan
# Date: 12/31/2019

# Old code for reference (basic setup, no interface)

# def salestaxcalc():
#    price = input('Please enter the price of the item you wish to purchase: \n')
#    price = float(price)
#    salestax = input('Please enter the tax rate for your state: \n')
#    salestax = float(salestax)
#    newprice = price + (price * salestax)
#    return newprice

def salestaxcalc():
    
    """Prompts a user for input for item price and sales tax rate and prints a new item price
    adjusted for sales tax"""
    
    print('This is a simple calculator designed to calculate prices of items with sales tax added.')
    loopvar = 1
    while loopvar != 0:
        price = input('Please enter the price of the item you wish to purchase: \n')
        price = float(price)
        salestax = input('Please enter the sales tax rate for your state: \n')
        salestax = float(salestax)
        newprice = price + (price * salestax)
        print("Price + Sales Tax = " + str(newprice))
        loopvar = input('Please enter 1 to calculate a new price, or enter 0 to exit the program.\n')
        loopvar = int(loopvar)

def statesalestax(taxrate):

    """Streamlined variant of salestaxcalc; takes tax rate (float) as an argument, prompts user for
    item price and prints a new item price adjusted for sales tax."""
    
    taxrate = float(taxrate)
    print("This is a simple calculator designed to calculate prices of items with sales tax added.")
    print("You have entered [" + str(taxrate) + "%] as your state's tax rate.\n")
    loopvar = 1
    while loopvar != 0:
        price = input("Please enter the price of the item you wish to purchase: \n")
        price = float(price)
        newprice = price + (price * taxrate)
        print("Price + Sales Tax = " + str(newprice))
        print("\n")
        loopvar = input("Please enter 1 to calculate a new price, or 0 to exit the program.\n")
        loopvar = int(loopvar)


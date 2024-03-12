# Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price.

def calculate_discount(price, discount_percent):
    discount = (100-discount_percent)/100
    discount_added = price*discount
    final = price - discount_added
    if discount_percent>=20:
        print("Original Price: {x}".format(x=price))
        print("Discount percentage: {x}".format(x=discount_percent))

        print("Final price: {y}".format(y=discount_added))
        return final
    
    elif discount_percent <20:
        print("Original Price: {x}".format(x=price))
        print("Discount percentage: {x}".format(x=discount_percent))

        print("Final price: {y}".format(y=discount_added))
        return price
    
    


calculate_discount(2000, 34)
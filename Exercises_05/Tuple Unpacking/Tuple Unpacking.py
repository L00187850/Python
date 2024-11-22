#Name: Philip Stewart
#Student Number: L00187850
#Date: 14 Nov 2024
#Purpose: Tuple unpacking


def most_expensive(price_list):
    """
    Iterate through a list and find the most expensive item
    """
    # Set up the variables
    max_price = 0
    max_price_item = ""
    # Iterate, unpacking the tuple
    for description, price in price_list:
        # If this is the maximum price, record that in our variables
        if price > max_price:
            max_price = price
            max_price_item = description
        # If it is not the maximum price, do nothing
        else:
            pass
    # Return the maximum prices item and its price
    return max_price_item, max_price

# Provide the data
price_list = [("Pineapple", 1.0), ("Apples", .5), ("Pears", .7), ("Peaches", .8)]
# Call the function and unpack its return values
# product, price  = most_expensive(price_list)
#Changed the penultimate line to the below:
product, price, availability = most_expensive(price_list)
print(product, price)

#Receiving the error "Traceback (most recent call last):
  #File "C:\Python\Exercises_05\Tuple Unpacking\Tuple Unpacking.py", line 31, in <module>
 # product, price, availability = most_expensive(price_list)
 #   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#ValueError: not enough values to unpack (expected 3, got 2)

#This basically explains that only two values were provided instead of three, which is what the code was expecting. the code was looking for a product (Pineapple), a price (1.0) and availability (doesn't exist)

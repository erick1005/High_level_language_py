from collections import OrderedDict
order = OrderedDict()  # Initialize an empty ordered dictionary

# Read a number of inputs
for _ in range(int(input())):  
    # Split the input into an item and a price
    item, space, price = input().rpartition(' ')  
    # Accumulate the price of each item
    order[item] = order.get(item, 0) + int(price)  

# Print out each item and its total price
for item, price in order.items():  
    print(item, price)

    '''input is 9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30'''
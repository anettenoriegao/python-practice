# Define variables
# Item number  name    price
# 1            Burger  $5.99
# 2            Pizza   $8.49
# 3            Salad   $4.99
# 4            Drink   $1.99

# Prices of menu options
burger_price = 5.99
pizza_price = 8.49
salad_price = 4.99
drink_price = 1.99

# Define dictionary (collection) - Menu - item + price
menu_items = {
    "1": ("Burger", burger_price),
    "2": ("Pizza",  pizza_price),
    "3": ("Salad",  salad_price),
    "4": ("Drink",  drink_price),
}

# Create collection for order/cart (we won't use it yet—STOP HERE step)
order = {}           # e.g., {"Burger": 2}
total_cost = 0.0     # running total (used later)

# # display welcome
# PRINT statement - WELCOME TO RESTAURANT
print("WELCOME TO RESTAURANT")

# Initiate while loop
while True:
    # display menu items (plain prints)
    print("Item | Name   | Price")
    print("---------------------")
    print("1    | Burger | $5.99")
    print("2    | Pizza  | $8.49")
    print("3    | Salad  | $8.49")
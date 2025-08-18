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

# # display welcome
# PRINT statement - WELCOME TO RESTAURANT
print("WELCOME TO RESTAURANT")

menu = {
    'Burger' : 5.99,
    'Pizza' : 8.49,
    'Salad' : 4.99,
    'Drink' : 1.99,
}
item_number = 1
for item, price in menu.items():
    print(f'{item_number}, {item}, ${price}')
    item_number += 1
    
# Initiate while loop
order_total = 0
while True:
    # display menu items (plain prints)
    print("Item | Name   | Price")
    print("---------------------")
    print("1    | Burger | $5.99")
    print("2    | Pizza  | $8.49")
    print("3    | Salad  | $4.99")
    print("4    | Drink  | $1.99")

    # prompt menu selection
    item_choice = input("Choose item:")

    #promp qty
    item_quantity = int(input("How many:"))

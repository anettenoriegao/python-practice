
# PRINT statement - WELCOME TO RESTAURANT
print("WELCOME TO RESTAURANT")

menu = {
       1 : {"name":"Burger","price": 5.99},
       2 : {"name":"Pizza","price": 8.49},
       3 : {"name":"Salad","price": 4.99},
       4 : {"name":"Drink","price": 1.99},
    }

# Initiate while loop
order_total = 0
item_number = 1


print("Menu")
for item_no, details in menu.items():
      print(f'{item_no}. {details["name"]} - ${details['price']}')

# prompt menu selection
    # Prompt menu selection (user input)
item_choice = input("Choose item number: ")

    # prompt qty
    # Prompt qty
item_qty = int(input("How many: "))



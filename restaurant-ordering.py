# program variables
menu = {
       1 : {"name":"Burger","price": 5.99},
       2 : {"name":"Pizza","price": 8.49},
       3 : {"name":"Salad","price": 4.99},
       4 : {"name":"Drink","price": 1.99},
    }
order_total = 0
item_number = 1
order = {}


# PRINT statement - WELCOME TO RESTAURANT
print("WELCOME TO RESTAURANT")


# Initiate while loop
while True:
   print("Menu")
   for item_no, details in menu.items():
         print(f'{item_no}. {details["name"]} - ${details['price']}')

   # prompt menu selection
      # take order (user input)
   item_choice = int(input("Choose item number: "))

      # Prompt qty
   item_qty = int(input("How many: "))

# add to order (by item number)
   if item_choice in menu:
        item_name = menu[item_choice]['name']
        if item_name in order:
             order[item_name] += item_qty
        else:
             order[item_name] = item_qty
   else:
        print("That is not a valid menu item.")

# continue ordering
   continue_order = input("Add another item? (Y/N):")
   if continue_order not in ("y","Y","yes"):
        break


   print(order)
   


empty_dict = {}
print(type(empty_dict))

product_prices = {
    'creamer' : 3.79,
    'apples' : 3.99,
    'pears' : 3.99
}

product_keys = product_prices.keys()
print(product_keys)

product_values = product_prices.values()
print(product_values)

product_items = product_prices.items()
print(product_items)

look_for = 'apples' in product_prices
print(look_for)

# restaurant-order

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

     # prompt
      # Prompt menu selection (user input)
    item_choice = input("Choose item number: ")

      
      # Prompt qty
    item_qty = int(input("How many: "))

    order = {
        23:{"name":"Burger","price":5.99},
        12:{"name":"Burger","price":5.99},
        1:{"name":"Burger","price":5.99},
   }
    
    order = {
    }

    if item_choice in menu:
        item_name = menu[item_choice]['name']

        if item_name[item_name] += item_qty
        else: 
            order[item_name] = item_qty

    print(f"Item name: {item_name}, qty {item_qty}")


    
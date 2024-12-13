"""
get number_of_items
for number_of_items
    get price_of_item
    add price_of_item to total_price
if total_price > $100
    apply 10% discount
print total_price

"""
total_price = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price_of_item = float(input("Price of item: $"))
    total_price += price_of_item
if total_price > 100:
    total_price -= (total_price * 0.1)  # Apply 10% Discount
print(f"Total price of {number_of_items} items is ${total_price:.2f}")

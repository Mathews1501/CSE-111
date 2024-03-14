import math

items = int(input("Enter the number of items: "))
items_in_box = int(input("Enter the number of items in the box: "))

boxes = math.ceil(items/items_in_box)

print(f'for {items} items, packing {items_in_box}, you will need {boxes}')


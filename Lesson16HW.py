shopping_list = {
    'milk' : 65,
    'bread' : 15,
    'coke' : 39,
    'cookie' : 45,
    'candy' : 24,
    'fruit' : 35.8
}

shopping_list['coke'] = 60
items = 0
payment = 0

for i in shopping_list:
    items += 1
    payment += shopping_list[i]
    
print('items:', items)
print('payment:', payment)
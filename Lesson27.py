'''list1 = [2, 5, 6, 7, 8, 9, 2, 9, 9]
list1.append(15)
list1.insert(4,20)
list1.pop(3)
print(list1)'''

'''for i in range(5):
    print(i, end='*')
print()'''

'''for i in range(1,6):
    for u in range(i):
        print('*', end='')
    print()'''

stuffs = [
    {"name": "笔记本电脑", "price": 9699},
    {"name": "主机", "price": 10999},
    {"name": "显示器", "price": 1999},
    {"name": "鼠标", "price": 929},
    {"name": "键盘", "price": 639},
    {"name": "耳机", "price": 999},
    {"name": "鼠标垫", "price": 399},
]

money = int(input('Enter the amount of money you have: '))

for i in range(len(stuffs)):
    print(f'{stuffs[i]["name"]}， 价格：{stuffs[i]["price"]} : [{i+1}]')

print()

price = 0

while True:
    stuff = int(input('Enter the number of the thing you want to buy[if you want to check out enter "0"]: '))

    if stuff == 0:
        break

    elif stuff > 7 or stuff < 0:
        print("stuff doesn't exist")

    
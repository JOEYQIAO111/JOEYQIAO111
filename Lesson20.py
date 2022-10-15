#Notes
'''
list
列表

dict
字典

int
数字

str
字符串

tuple
元组

set
集合


数字运算符：
= 赋值
% 取余
// 整除
/ 除
* 乘
** 次方


反转： [::-1]

'''

#Practice
'''a = int(input())
b = int(input())
c = int(input())
print()
if a > b and a > c:
    print(a)

elif b > c and b > a:
    print(b)

elif c > b and c > a:
    print(c)'''

'''a = [0,0,0]
for i in range(3):
    a[i] = int(input())
print(max(a))'''

'''a = []
n = int(input('How many numbers do u want to enter? : '))
for i in range(n):
    num = int(input())
    a.append(num)
print(max(a))'''

'''max_num = 0
n = int(input('How many numbers do u want to enter? : '))
for i in range(n):
    num = int(input())
    if num > max_num:
        max_num = num
print(max_num)'''

'''a = input('Enter numbers or letters: ')

count = 0
for i in a:
    if i.isdigit():
        count += 1
print(count)'''


import random
a = []
for i in range(1000):
    number = random.randint(1,100)
    a.append(number)
a.sort()
b = {}
for i in a:
    keys = list(b.keys())
    if i in keys:
        b[i] += 1
    else:
        b[i] = 1
print(b)
'''#元组
t1 = (1,2,3)'''

#return 使用方法
'''def fun1(a,b):
    c = a + b
    d = a - b
    return c, d

print(fun1(2,3))'''

#keys values items
dict1 = {
    '1' : 'a',
    '2' : 'b',
    '3' : 'c'
}

print(dict1.keys())
print(dict1.values())
print(dict1.items)

#查看字典
'''dict = {
    '1' : 'a',
    '2' : 'b',
    '3' : 'c'
}

for k in dict.keys():
    print(k, end = '')
print()

for v in dict.values():
    print(v, end = ' ')
print()

for i in dict.items():
    print(i, end = ' ')
print()
'''
'''dict1 = {'Tom' : 98, 'Eric' : 88, 'Cythia' : 90}

for i in dict1.items():
    print(i)

for key,value in dict1.items():
    print(key, ':', value)'''

#Practice
'''dict = {
'Abbi': 497,
'Alexia': 552,
'Gabby': 382,
'Kacie': 550,
'Taban': 329,
'Pablo': 289,
'Jamal': 544,
'Fabian': 493,
'Ebenezer': 301
}

for key,value in dict.items():
    if value < 400:
        value = '不及格'
    elif value >= 500:
        value = '优秀'
    else:
        value = '及格'
    print(key, ':', value)
    print()'''
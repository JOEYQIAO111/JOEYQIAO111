'''li = ['a', 'b', 'c']
del li[1:3]
print(li)'''

'''l1 = [11, 22, 33]
l2 = [22, 33, 44]

for i in l1:
    if i in l2:
        print(i)
        
for i in l1:
    for j in l2:
        if i == j:
            print(i)'''

#乘法表
'''for i in range(1,10):
    for u in range(1,10):
        a = i * u
        print(u, '*', i,  '=', a)'''

#/t = tab
#/n = return
#end = ' ' = no return

li = [11,22,33,44,55,66,77,88,99,90]

dic = {}

dic['>66'] = []
dic['<66'] = []

for i in li:
    if i > 66:
        dic['>66'].append(i)
    elif i < 66:
        dic['<66'].append(i)

print(dic)
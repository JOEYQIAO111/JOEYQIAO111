'''a = ['1', '2', '3', '4']
for i in range(len(a)):
    a[i] = int(a[i])
print(a)'''

'''list1 = [1, 2, 3]
tuple1 = (1, 2, 3)

for i in tuple1:
    print(i)'''

'''dic = {
    'C1' : 'C1.1, C1.2, C1.3',
    'C2' : 'C2.1, C2.2, C2.3',
    'C3' : 'C3.1, C3.2, C3.3'
}

dic['C4'] = 'C4.1'

del dic['C4']

print(dic)'''

dic = {
    'C1' : 'C1.1, C1.2, C1.3',
    'C2' : 'C2.1, C2.2, C2.3',
    'C3' : 'C3.1, C3.2, C3.3'
}

dic['C4'] = 'C4.1, C4.2, C4.3'

dic['C3'] = 'C3.1, C3.5, C3.3'

print(dic)
# Notes
'''a = 1
print(type(a))'''

'''a = 11
print(float(a))
'''

'''qwer = 'abcd'
print(qwer[0])'''

'''qwer = 'abcd'
for i in qwer:
    print(i, end=' ')
print()'''

'''str1 = 'abcd'
for i in range(len(str1)):
    print(str1[i])'''

'''str1 = 'abcd'
print(str1[1:4])'''

'''str1 = 'abcd'
print(str1[:])'''

'''str1 = 'qwertyuiopasdfghjklzxcvbnm'
print(str1[:-3])'''

'''str1 = 'abcde'
print(str1[::-1])'''

'''str1 = 'abcde'
print(str1[::3])'''

'''list1 = [1,3,4,'a', 't', [1,2]]
print(list1)'''


#append insert extend count remove index


'''list1 = [1,2,3,4]
list1.append('a')
print(list1)'''

'''list1 = [1,2,3,4]
print(list1[::-1])'''

'''list1 = [1,2,3,4]
list1.insert(1,'a')
print(list1)'''

'''list1 = [1,2,3,4]
list2 = ['a','b','c']
list1.extend(list2)
print(list1)'''

'''list1 = [1,2,3,4,1,5,6,7,8,9,1]
print(list1.count(1))'''

'''list1 = [1,2,3,4,1]
list1.remove(1)
list1.remove(1)
print(list1)'''

'''list1 = [1,2,3,4]
print(list1.index(4))'''

#Practice
'''students = ['Master Yi', 'Yasuo', 'Jinx', 'VI', 'Caitlyn', 'Garen', 'Lee Sin', 'Jayce', 'Wukong', 'Ekko']
students1 = []
students2 = []
for i in students:
    if len(i) % 2 == 0:
        students2.append(i)
    if len(i) % 2 != 0:
        students1.append(i)
print(students1)
print(students2)'''
#notes
'''
set

set1 = {'a', '1', 1, 1, 2, 3}
for i in set1:
    print(i)
print()
print(len(set1))
print()
print(set1)

list1 = [1,2,5,1,3,2]
print(list(set(list1)))


'''
#practice

'''list1 = [1,3,5,7,9]
list1.remove(5)
list1[0] = list1.pop(2)
print(list1)'''

'''list1 = [1, 3, 7, 5, 9]
a = list1.pop(0)
list1[0] = list1.pop(a)
print(list1)'''

'''def a(number):
    count = 0

    for i in range(number + 1):
        count += i
    
    return count

b = a(10)
print(b)'''

'''def a(l1):
    max_n = 0
    for i in l1:
        if i > max_n:
            max_n = i
            
    return max_n

b = a([1, 2, 3, 4, 5])
print(b)'''
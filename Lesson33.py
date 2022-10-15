#11, 1不能倒着走所以要加-1
'''for i in range(11, 1, -1):
    print(i)'''
#11,10,9,8,7,6,5,4,3,2
'''for i in range(1, 11, 2):
    print(i)'''
#1, 3, 5, 7, 9

'''list1= [i for i in range(1,101)]
print(list1)'''

username = 'J'
password = 'qwer'

def login(user, passw):
    if user == username and passw == password:
        return True, 'True'
    return False, 'False'

user = input('Username: ')
passw = input('Passsword: ')

result = login(user, passw)

print(result)
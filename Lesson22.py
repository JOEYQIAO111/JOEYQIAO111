#Notes
'''def a(str1):
    if not str1:
        return 'None'

    else:
        return 'True'

result = a('1')
print(result)'''

#Practice
'''def a(b):
    if len(b) > 2:
        c = b[:2]
        return c
    
    return b

d = a([1,2,3])

print(d)'''

user_info = {'Username' : '', 'Password' : ''}

def sign_up():
    print('————————————————————————————————————')
    print('Welcome to MIW sign up page')
    print('————————————————————————————————————')
    username = input('Enter username: ')
    password = input('Enter password: ')
    
    user_info['Username'] = username
    user_info['Password'] = password

def login():
    for i in range(3):
        print('————————————————————————————————————')
        print('Welcome to MIW login page')
        print('————————————————————————————————————')
        Username = input('Enter username: ')
        Password = input('Enter password: ')

        if Username == user_info['Username'] and Password == user_info['Password']:
            print('————————————————————————————————————')
            print('Welcome back ' + user_info['Username'])
            break
        print('————————————————————————————————————')
        print('Wrong password or username')

sign_up()
login()
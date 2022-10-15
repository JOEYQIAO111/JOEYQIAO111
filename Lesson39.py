'''with open('a.txt', 'w') as f:
    for i in range(101):
        f.write(f'{i}\n')'''

'''import random
with open('电话.txt', 'w') as f:
    for i in range(1000):
        b = '%08d' % random.randint(0, 99999999)
        f.write(f'186{b}\n')'''

while True:
    status = True
    with open('loginfo.txt', 'a+') as f:
        username = input('Enter username: ')

        a = f.readlines()
        print(a)
        for i in range(0, len(a), 2):
            if username == i:
                print('username already exist')
                status = False

        password = input('Enter password: ')
        passwordc = input('Check password: ')

        if password == passwordc and status == True:
            f.write(username + '\n')
            f.write(password + '\n')
            break

        else:
            print('password is not the same')
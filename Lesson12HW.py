usernames = ['JOEYQIAO111', 'filthymudblood111', 'yi.qiao']
passwords = ['1234qwer!@#$QWER', '1234567890', 'qwertyuiop']

username = input('Username: ')

if username in usernames:
    password = input('Password: ')

    if username == 'JOEYQIAO111' and password == '1234qwer!@#$QWER':
        print('Welcome')
    if username == 'JOEYQIAO111' and password != '1234qwer!@#$QWER':
        print('Wrong password or username')

    if username == 'filthymudblood111' and password == '1234567890':
        print('Welcome')
    if username == 'filthymudblood111' and password != '1234567890':
        print('Wrong password or username')

    if username == 'yi.qiao' and password == 'qwertyuiop':
        print('Welcome')       
    if username == 'yi.qiao' and password != 'qwertyuiop':
        print('Wrong password or username')       
else:
    print('Username does not exist')
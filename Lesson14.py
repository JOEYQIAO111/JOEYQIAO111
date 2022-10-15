#Notes
list1 =  [1,2,3]
list1.pop(1)
print(list1)

'''name = 'Joey'
print('My name is %s, age is %d' % (name,18))'''

#MIW Login 
'''Usernames = ['D', 'J', 'Q', 'Y']
Passwords = ['857857','1234qwer!@#$QWER', 'qianqian', 'wangzili']

admin = 'xadmin'
admin_password = '!@#$%^&*()'

print('     Welcome to MIW home page     ')

Username = input('Username: ')
Password = input('Password: ')

if Username != admin or Password != admin_password:
    print('Wrong password of username')
    Username = input('Username: ')
    Password = input('Password: ')
if Username == admin and Password == admin_password:
    while True:
        print(''     Admin page     
                Add member(1)
                Delete member(2)
                View member info(3)
                Quit(4)'')
        number = input('Enter the number: ')

        if number == '1':
            new_member_username = input("Enter the new member's username: ")
            new_member_password = input("Enter the new member's password: ")
            
            Usernames.append(new_member_username)
            Password.append(Password)

            print('Adding new member successful')
        
        elif number == '2':
            print(Usernames)
            print(Passwords)

            deleted_user = int(input('Enter which user you want to delete: '))
            if deleted_user not in Usernames:
                print('Please enter th correct username')
            else:
                delete_usernames_index = Usernames.index(deleted_user)
                Usernames.remove(deleted_user)
                Password.remove(delete_usernames_index)
        
        elif number == '3':
            print(Usernames)
            print(Passwords)
        
        elif number == '4':
            break

        else:
            print('Please enter the correct command')'''
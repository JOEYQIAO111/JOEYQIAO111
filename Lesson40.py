'''def signup():
    while True:
        status = True
        with open('loginfo.txt', 'a+') as f:
            username = input('Enter username: ')

            with open('loginfo.txt', 'r') as r:
                a = r.readlines()
                for i in range(0, len(a), 2):
                    if username == a[i].strip():
                        print ('username already exist')
                        status = False
                                        
            if status == True:
                password = input('Enter password: ')
                passwordc = input('Check password: ')

                if password == passwordc:
                    f.write(username + '\n')
                    f.write(password + '\n')
                    break

                else:
                    print('Password is not the same')
signup()'''

#可以试这个代码有没有错，如果有错就会运行except下面的代码
try:
    pass
except:
    pass
else:
    pass
    #如果没错就运行这块
finally:
    pass
    #有没有异常都运行这块
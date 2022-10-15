'''usernames = ['JOEYQIAO111', 'filthymudblood111', 'yi.qiao']
passwords = ['1234', 'qwer', 'wasd']

username = input('Username: ')

if username not in usernames:
    print('username does not exist')

if username in usernames:
    for i in range(3):
        password = input('password: ')
        username_index = usernames.index(username)
        password1 = passwords[username_index]
            
        if password1 == password:
            print('Welcome back!')
            break
        if password1 != password:
            print('Wrong password or username')'''

#Minecraft blocks
'''new_blocks = ['远古残骸', '玄武岩', '黑石', '黑石台阶', 
'黑石楼梯', '黑石墙', '锁链', '錾制下界砖块', '裂纹下界砖块', 
'绯红菌', '诡异菌', '绯红菌岩', '诡异菌岩', '绯红木板', '诡 异木板', 
'绯红菌索', '诡异菌索', '绯红菌柄', '诡异菌柄', '绯红菌核', '诡异菌核', 
'哭泣的黑 曜石', '镶金黑石', '磁石', '下界金矿石', '下界苗', '下界合金块', 
'磨制玄武岩', '磨制黑石', '磨制黑石砖', '磨制黑石按钮', '磨制黑石压力板', '磨制黑石台阶', 
'磨制黑石楼梯', '磨制黑石墙', '錾制磨制黑石', '磨制黑石砖台阶', '磨制黑石砖楼梯', '磨制黑石砖墙', 
'裂纹磨制黑石砖', '石英砖', '重生锚', '菌光体', '灵魂营火', '灵魂火', '灵魂灯笼', '灵魂土', 
'灵魂火把', '标 靶', '缠怨藤', '诡异疣块', '垂泪藤']

block = []
for i in new_blocks:
    if '下界' in i or '绯红' in i:
        block.append(i)
print(block)'''

'''import random
list = ['a', 'b', 'c']
for i in range(3):
    a = random.choice(list)
    print(a)'''

import random
questions = 0
s = ['*', '+', '-']
while questions < 10:
    number1 = random.randint(0,10)
    number2 = random.randint(1,10)
    s = random.choice(s)
    print(str(number1) + s + str(number2))
    if s == '+':
        answer = number1 + number2
    elif s == '*':
        answer = number1 * number2
    else:
        answer = number1 - number2
    result = int(input('Enter the answer: '))
    if result == answer:
        print('correct')
    elif result != answer:
        print('Wrong answer')
        print('The correct answer is: ',answer)
    questions += 1
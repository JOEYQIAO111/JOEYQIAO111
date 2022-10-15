'''dic = {}

def add(name, phone):
    if name not in dic:
        dic[name] = phone
        print('好友添加成功')
    else:
        print('好友已存在')

def delete(name):
    if name in dic:
        del dic[name]
        print('好友删除成功')
    else:
        print('好友不存在')

def changep(name, nphone):
    if name in dic:
        dic[name] = nphone
        print('修改完成')
    else:
        print('好友不存在')

def changen(name, nname, phone):
    if name in dic:
        del dic[name]
        dic[nname] = phone
        print('修改完成')
    else:
        print('好友不存在')


while True:
    print()
    print('——————J电话册——————')
    print()
    print('————添加好友[1]————')
    print('————删除好友[2]————')
    print('————显示好友[3]————')
    print('————修改好友[4]————')
    print('——————退出[5]——————')
    print()

    inp = int(input('输入数字：'))
    print()

    if inp == 1:
        name = input('输入新好友名称：')
        phone = int(input('输入新好友电话号码：'))
        add(name, phone)

    elif inp == 2:
        name = input('输入要删除的好友的名称：')
        delete(name)

    elif inp == 3:
        if len(dic) != 0:
            print(dic)
        else:
            print('没有好友')
    
    elif inp == 4:
        name = input('输入想要修改的好友：')

        print('修改名称[1]')
        print('修改电话[2]')

        inp1 = int(input('输入数字：'))

        if inp1 == 1:
            nname = input('输入好友的新名称：')
            phone = dic[name]

            changen(name, nname, phone)
        
        elif inp1 == 2:
            nphone = input('输入好友的新电话：')

            changep(name, nphone)
    
    else:
        break'''

'''inp = input()
num = '1234567890'
a = ''
for i in inp:
    if i not in num:
        a = a + i

print(a)'''

'''f = open('D:\PC\Python\Practice_page.py')
print(f.read())'''

'''with open('D:\PC\Python\Practice_page.py') as f:
    content = f.read()
    print(content)'''

f = open('D:\PC\Python\pi_digits.txt')
b = ''
a = f.readlines()
for i in a:
    b += i[:-2]
print(b)
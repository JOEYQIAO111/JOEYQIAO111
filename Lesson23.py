'''使用input函数接收用户的输入,用户输入一个年份,请写代码判断这一年是否为闰年,
如果是闰年,则输出“xxx 是闰年”,反之输出“xxx 不是闰年”, 闰年的规则如下:

不能被4整除的一定不是闰年
如果年份能被4整除且不能被100整除,则是闰年
如果年份能被4整除,同时又能被100整除,那么要判断它能否被400整除,如果可以则是闰年，否则不是'''

'''def a(year):
    if year % 4 == 1:
        b = '闰年'
    else:
        b = '平年'
    return b

year = int(input('Enter a year: '))

c = a(year)

print(c)'''


'''def a(stuff):
    if stuff[::-1] == stuff:
        b = '是回文'
    else:
        b = '不是回文'

    return b
stuff = input('Enter anything: ')

c = a(stuff)
print(c)'''

'''def a(num):
    num.sort()
    for i in range(11):
        if i not in num:
            print(i)


c = a([1, 3, 2, 4, 6, 9, 0, 8, 10, 7])'''


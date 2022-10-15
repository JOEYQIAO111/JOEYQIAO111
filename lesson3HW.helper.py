# 输入函数input()
"""
    默认类型:String
    类型转换:
        1.整型:int(input())
        2.小数类型:float(input())"""
# 加法计算器
'''print("加法计算器")
a = int(input("请输入a："))
b = int(input("请输入b："))
print("a+b=",a+b)
'''

# input()输入边长，绘制正方形
'''import turtle
a = int(input("请输入边长:"))
t = turtle.Pen()
t.color('red')
for i in range(4):
    t.fd(a)
    t.left(90)
turtle.done()
'''

# input()输入符号，绘制正方形
'''
a = input("请输入符号:")
print(a)
print(a*2)
print(a*3)
'''
import random
number = int(input("请输入数字"))
a = random.randint(1, 10)
for i in range(10):
    if a == number:
        print("我猜是:", a)
        print("猜对啦")
        break
    elif a > number:
        print("我猜是:", a)
        print("猜大了")
        a = random.randint(1 ,a)
    else:
        print("我猜是:", a)
        print("猜小了")
        a = random.randint(a, 10)
if a == number:
    print("游戏成功")
else:
    print("游戏失败")
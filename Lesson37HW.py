"""
2022.8.27课堂总结
1.回顾了列表中的insert、extend、
remove、pop、de、reverse方法
2.学习了如何判断一个元素是否存在列表或字典中
3.回顾了了函数的定义以及使用
4.学习了字典中的keys、values、items方法
5.完成了课堂练习
"""

li = [['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']]

# 1.将列表li中的'tt'变成大写

# 2.将列表中的数字3变成字符串'100'

# 3.将列表中的字符串'1'变成数字101

li[0][1][2]['k1'][0] = 'TT'

li[0][1][2]['k1'][1] = '100'

li[0][1][2]['k1'][2] = 101

print(li)
students = [
    {'name':'A','age':18,'score':98,'tel':'18888888888','gender':'female'},
    {'name':'B','age':20,'score':95,'tel':'18888888889','gender':'unknown'},
    {'name':'C','age':18,'score':88,'tel':'18888888810','gender':'male'},
    {'name':'D','age':16,'score':58,'tel':'18888888811','gender':'unknown'},
    {'name':'E','age':19,'score':78,'tel':'18888888812','gender':'male'},
    {'name':'F','age':17,'score':92,'tel':'18888888813','gender':'male'},
]
age_count = 0
score_count = 0
name_n = ''
score_n = 0
score_l = []

for i in students:
    name = i['name']
    score = i['score']
    age = i['age']
    tel = i['tel']
    gender = i['gender']

    if score < 60:
        print('不及格： ', name, ': ', score)
        score_count += 1

    if age < 18:
        age_count = age_count + 1

    if tel[-1] == '8':
        print('手机尾号是8的同学： ' + name)

    if score > score_n:
        score_n = score
        name_n = name
    
    if gender == 'unknown':
        students.remove(i)

print('不及格个数：', score_count)
print('未成年人数量：', age_count)
print('最高分： ', name_n , ': ', score_n)
print(students)
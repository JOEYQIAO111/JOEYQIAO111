import random

'''l1 = []

for i in range(100000):
    l1.append(random.randint(0,1))

print(l1.count(1), l1.count(0))'''

'''l1 = [random.randint(0,1) for i in range(100)]
print(l1.count(0), l1.count(1))'''

'''l1 = [i for i in range(1, 21)]
print(l1)'''

'''l1 = [i**3 for i in range(1, 21)]
print(l1)'''

'''l1 = [i if i % 3 == 0 else -i for i in range(101)]
print(l1)'''

'''color = ['b', 'w']
size = ['S', 'M', 'L', 'XL']

for i in color:
    for u in size:
        print(i, u)'''

'''color = ['b', 'w']
size = ['S', 'M', 'L', 'XL']

l1 = [(i, u) for i in color for u in size]
print(l1)'''

'''l1 = [[0 for i in range(10)] for j in range(10)]
print(l1)'''

'''shape = ['♥', '♦', '♣', '♠']
l1 = [(u, i) for i in range(2, 11) for u in shape]
print(l1)'''

'''a = 'nfwirpfubnruskfbhgtieiruwowpwpirugthbbbcnmxmvcsfivhvhsjfrkslifrjuebvbvndxlfrjsbbjfckslrrhshbfrjedkdjfnvbxnfworigfuhgjskcnvgbdjedjglsbgfuekifdngndldngbf' 
dic = {}

for i in a:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
print(dic)'''

'''dic = {
    'a' : 1,
    'b' : 2,
    'c' : 3
}

print(sum(dic.values()))'''

'''for k in dic.keys():
         dic.values
         dic.items'''
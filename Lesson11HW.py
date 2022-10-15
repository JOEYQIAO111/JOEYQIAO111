n = int(input('Enter a whole number: '))
con = 0
max = 0
while n > 0:
    if n % 10 == 0:
        con = con + 1
    elif n % 10 != 0:
        if n % 10 > max:
            max = n % 10
    n = n // 10
print('number of zeros: ',con,'the max is: ',max)
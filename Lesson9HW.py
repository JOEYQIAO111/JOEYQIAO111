# Guessing number 2.0
'''import random
number = random.randint(0,100)
tries = 1
print('You have infinity tries')
a = int(input('Guess a number between 0 and 100: '))
while a != number:
    if a == number:
        print('You got it!')
        break
    if a < number:
        print('Too small')
    if a > number:
        print('Too big')
    if a > 100:
        print('You can not guess numbers bigger then 100! Good Bye')
        break
    if a < 0:
        print('You can not guess numbers smaller then 0! Good Bye')
        break
    tries = tries + 1
    a = int(input('Guess a number between 0 and 100: '))
if a == number:
    print('You got it! ')
    print('You used',tries,'tries')'''
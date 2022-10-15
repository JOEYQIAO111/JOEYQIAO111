import random
number = random.randint(0,10)
print('Think a number between 0 and 10, I will try and guess the number in 5 tries, each time I guess a number you need to type too big, if the number is too smal then type too small')
print(number)
for i in range(5):
    number1 = random.randint(number,10)
    number2 = random.randint(0,number)
    a = input('Is the number the right number? Or is it too small or too big?(you got it/too small/too big): ')
    if a == 'too small':
        print(number1)
    if a == 'too big':
        print(number2)
    if a == 'you got it':
        print('yeah I win!')
        break
if a != 'you got it':
    print('I lost')

'''import random
a = int(input('Enter a number between 1 and 10: '))
number = random.randint(1,10)
for i in range(4):
    if number == a:
        print('My guess is ', number)
        print('I win')
        break
    elif number < a:
        print('My guess is ', number)
        print('Too small')
        number = random.randint(number,10)
    else:
        print('My guess is ', number)
        print('Too big')
        number = random.randint(1,number)
print('Game over')'''
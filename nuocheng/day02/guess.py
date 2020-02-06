import random
num = random.randint(1, 100)
counter = 0
while counter < 7:
    counter += 1
    answer = int(input('guess: '))
    if answer == num:
        print('guess right')
        break
    if answer > num:
        print('guess bigger')
    else:
        print('guess smaller')
else:
    print('right answer is:', num)
    print('right answer is: ' + str(num))
    print('right answer is: %s' % num)
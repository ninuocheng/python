# import star
# print(star.name)
# print(star.hi)
# star.pstar(10)
# from random import choice, randint
# print(choice('abcd'))
# print(randint(1, 100))
# import star
# print(star.hi)
# star.pstar()
# from random import choice, randint
# print(choice('1234567890'))
# print(randint(1, 100))
# import sys, getpass
# import getpass as gp
# upass = gp.getpass()
# print(upass)
import random, sys
str1 = 'abcdefghijklmnopqrstuvwxyz0123456789.,/;\=+-)(*&^%$#@!~`<>?":)'
def fun2(n = 8):
    pas = ''
    while 1:
        ps = random.choice(str1)
        pas += ps
        if len(pas) == n:
            break
    return pas
if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(fun2(int(sys.argv[1])))
    else:
        print(fun2())
# import sys
# if len(sys.argv) == 1:
#     print('true')
# else:
#     print('false')
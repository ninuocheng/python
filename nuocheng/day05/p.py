import random, sys
from string import ascii_letters, digits

ch = ascii_letters + digits


def mk_pass(n=4):
    result = ''
    while 1:
        ps = random.choice(ch)
        result += ps
        if len(result) == int(n):
            return result


def mk_ps(m=6):
    result = ''
    for i in range(m):
        p1 = random.choice(ch)
        result += p1
    return result


def mk_ps1(q=10):
    result = 0
    count = 1
    for i in range(q+1):

        if count < q + 1:
            result += count
            count += 1
            continue
        return result
    # return result

def mk_ps2(y=2):
    result = ''
    for i in range(y):
        p3 = random.choice(ch)
        result += p3
    return result


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(mk_pass(sys.argv[1]))
    else:
        print(mk_pass())
if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(mk_ps(int(sys.argv[1])))
    else:
        print(mk_ps())
if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(mk_ps1(int(sys.argv[1])))
    else:
        print(mk_ps1())
if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(mk_ps2(int(sys.argv[1])))
    else:
        print(mk_ps2())

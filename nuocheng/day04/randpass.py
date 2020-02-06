import random, sys
from string import ascii_letters, digits
all_chs = ascii_letters + digits
def randpass(n = 6):
    result = ''
    for i in range(n):
        ch = random.choice(all_chs)
        result += ch
    return result
if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(randpass(int(sys.argv[1])))
    else:
        print(randpass())
import random
from string import ascii_letters, digits
ch = ascii_letters + digits
def mk_pas():
    pas = ''
    while 1:
        p = random.choice(ch)
        pas += p
        if len(pas) == 8:
            break
    return pas
if __name__ == '__main__':
    print(mk_pas())
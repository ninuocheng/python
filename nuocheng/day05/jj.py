for i in range(10):
    for j in range(1, i + 1):
        print('\033[31m%sx%s=%-3s\033[0m' % (j, i, i * j), end='')
    print('')
for i in range(10):
    for j in range(1, i + 1):
        print('\033[34m%sx%s=%-3s\033[0m' % (j, i, i * j), end='')
    print('')
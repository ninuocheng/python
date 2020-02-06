for i in range(1, 10):
for j in range(1, i + 1):
    # print('%s%s%s%s%-3s' % (j, 'x', i, '=', i * j), end='')
    print('%sx%s=%-3s' % (j, i, i * j), end='')
print('')
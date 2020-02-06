# l = [0, 1]
# n = int(input('length: '))
# for i in range(n - 2):
#     l.append(l[-2] + l[-1])
# print(l)
# print([5])
# print([5 + 5])
# print([5 + 5 for i in range(10)])
# print([5 + i for i in range(11)])
# print([5 + i for i in range(12) if i % 2])
# print([5 + i for i in range(12) if i % 2 == 0])
# for i in range(1, 255):
#     print('192.168.1.' + str(i))
print(['192.168.1.%s' % i for i in range(1, 255)])
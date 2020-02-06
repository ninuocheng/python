# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print('%sx%s=%s' % (j, i, i * j), end=' ')
#     print()
# f = open('/tmp/passwd')
# data = f.read()
# print(data)
# f.close()
# f = open('/tmp/passwd')
# print(f.read(4))
# print(f.read(6))
# print(f.readline())
# print(f.readline())
# print(f.readlines())
# print(type(f.readlines()))
# f.close()
# f = open('/tmp/passwd')
# for i in f:
#     print(i, end='')
# f.close()
f1 = open('/tmp/bj.jpg', 'rb')
print(f1.read(10))
f1.close()
f2 = open('/tmp/hi.txt', 'rb')
print(f2.read())
#一个英文字符正好占一个字节，就用英文字符本身去显示；但是一个汉字在utf8编码中占3字节，没有办法把一个字节表示成字符，所以就用16进制数表示
f2.close()
s1 = b'\xe8\xbe\xbe'
print(s1)
print(s1.decode()) #将bytes类型转成str类型
s2 = '达'
print(s2.encode()) #将str类型转成bytes类型
t = '方泽鑫'
print(t.encode())
y = b'\xe6\x96\xb9\xe6\xb3\xbd\xe9\x91\xab'
print(y.decode())
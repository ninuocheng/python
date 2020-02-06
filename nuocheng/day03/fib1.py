# def mk_fib():
#     fib = [0, 1]
#     n =int(input('长度: '))
#     for i in range(n - 2):
#         fib.append(fib[-1] + fib[-2])
#     print(fib)
# mk_fib() #调用函数时，必须用（），调用函数就是执行函数内的代码
# mk_fib()
# def add():
#     result = 10 + 20
# a = add()
# print(a)
# def add2 ():
#     a = 10
#     b = 20
#     result1 = 10 + 20
#     result2 = 10 * 20
#     return 'hello world'
# b = add2()
# # print(b)
# def mk_fib1():
#     fib = [0, 1]
#     n = int(input('长度: '))
#     for i in range(n - 2):
#         fib.append(fib[-2] + fib[-1])
#     return fib
# list = mk_fib1()
# print(list)
# def add3():
#     a = 10长度
#     b =20
#     return a + b
# c = add3()
# print(c)
# def mk_fib():
#     fib = [0, 1]
#     n = int(input('长度: '))
#     for i in range(n - 2):
#         fib.append(fib[-2] + fib[-1])
#     return fib
# a = mk_fib()
# b = [i * 2 for i in a]
# print(b)
# with open('/tmp/fib.txt', 'w') as fobj:
#     fobj.write(str(a))
def mk_fib(n):
    fib = [0, 1]
    for i in range(n - 2):
        fib.append(fib[-2] + fib[-1])
    return fib
a = mk_fib(5)
b = [i * 2 for i in a]
print(b)
with open('/tmp/fib.txt1', 'w') as fobj:
    fobj.write(str(a))
n = int(input('长度: '))
c = mk_fib(n)
print(c)
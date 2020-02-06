# s = 'python'
# for ch in s:
#     print(ch)
# print('*' * 30)
# users = ['tom', 'jerry', 'bob']
# for name in users:
#     print(name)
# print('*' * 30)
# nums = (10, 20, 30)
# for i in nums:
#     print(i)
# print('*' * 30)
# adict = {'name': 'gzc', 'age': 29}
# for key in adict:
#     print(key, adict[key])
# print(range(10))
# print(list(range(10)))
# for i in range(10):
#     print(i)
# print(list(range(6, 11)))
# print(list(range(1, 11, 2)))
# print(list(range(10, 0, -1)))
# result = 0
# for i in range(1, 10000001):
#     result += i
# print(result)
import sys
def add_num(n=100):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result
if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(add_num(int(sys.argv[1])))
    else:
        print(add_num())


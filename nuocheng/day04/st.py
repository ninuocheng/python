s = '   \thello world!\thow are you\t   '
print(s.strip())  #去除字符串两端空白字符
print(s.lstrip())  #去除字符串左端空白字符
print(s.rstrip())#去除字符串右端空白字符
print(s.center(60))#居中
print('hello'.center(30, '*'))
print('hello'.rjust(30, 'a'))
print('hello'.ljust(30, 'b'))
print(s.upper())#转大写
print('hELLO WORLD'.lower())#转小写
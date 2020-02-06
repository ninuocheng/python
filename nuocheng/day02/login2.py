# import getpass
# un = input('username: ')
# password = getpass.getpass('passd: ')
# if 'bob' == un:
#     if password == '123456':
#         print('Login successful')
#     else:
#         print('Login incorrect')
# else:
#     print('Login incorrect')
import getpass
un = input('username: ')
password = getpass.getpass('secret: ')
if un == 'bob' and password == '123456':
    print('Login successful')
else:
    print('Login incorrect')
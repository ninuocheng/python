try:
    num = int(input('number: '))
    result = 100 / num
    print('Done')
except ValueError:
    print('无效的输入')
except ZeroDivisionError:
    print('无效的输入')
except KeyboardInterrupt:
    print('\nBye-bye')
except EOFError:
    print('\nBye-bye')
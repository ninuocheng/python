try:
    num = int(input('number: '))
    result = 100 / num
    print(result)
    print('Done')
except (ValueError, ZeroDivisionError) as e:
    print('无效的输入', e)
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
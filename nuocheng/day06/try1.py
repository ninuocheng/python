try:
    num = int(input('number: '))
    result = 100 / num
except (ValueError, ZeroDivisionError) as e:
    print('无效的输入:', e)
except (KeyboardInterrupt, EOFError):
    print('\nBye-bye')
    exit(101)
else:
    print(result)
finally:
    print('一定要执行的语句')
print('Done')
users = ['tom', 'jerry', 'bob']
a = enumerate(users)
if __name__ == '__main__':
    for data, name in a:
        print(data, name)
import getpass
adict = {}


def new_user():
    user = input('用户名: ').strip()
    if user:
        if user not in adict:
            # passwd = input('密码: ').strip()
            getpass.getpass
            if passwd:
                adict[user] = passwd
                print('注册成功')
            else:
                print('\033[31;1m密码输入为空,请重新输入.\033[0m')
        else:
            print('\033[31;1m用户已注册,请重新输入.\033[0m')
    else:
        print('输入为空,请重新输入.')


def old_user():
    user = input('用户名: ').strip()
    if user:
        passwd = input('密码: ').strip()
        if user in adict:
            if adict[user] == passwd:
                print('\033[31;1m登录成功\033[0m')
            else:
                print('登陆失败')
        else:
            print('登陆失败')
            print(1)
    else:
        print('输入为空,请重新输入.')


def show_menu():
    prompt = """(0): 注册
(1): 登录
(2): 退出
请选择(0/1/2): """
    cmds = {'0': new_user, '1': old_user}
    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print('\033[31;1m无效的参数,请重试.\033[0m')
            continue
        if choice == '2':
            print('\033[31;1mbye-bye\033[0m')
            break
        cmds[choice]()


if __name__ == '__main__':
    show_menu()

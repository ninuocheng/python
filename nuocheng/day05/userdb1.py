import getpass

userdb = {}


def register():
    username = input('\033[31;1m用户名: \033[0m').strip()
    if not username:
        print('\033[34;1m用户名不能为空,请重新输入.\033[0m')
    elif username in userdb:
        print('\033[31;1m用户已存在.\033[0m')
    else:
        password = input('\033[31;1m密码: \033[0m')
        userdb[username] = password
        print('\033[31;1m注册成功.\033[0m')


def login():
    username = input('\033[31;1m用户名: \033[0m').strip()
    password = getpass.getpass('\033[31;1m密码: \033[0m')
    if userdb.get(username) == password:
        print('\033[31;1m登录成功.\033[0m')
    else:
        print('\033[31;1m登陆失败.\033[0m')


def show_menu():
    cmds = {'0': register, '1': login}
    prompt = """\033[31;1m(0) 注册
(1) 登录
(2) 退出
请选择(0/1/2): \033[0m"""
    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print('\033[34;1m无效的输入,请重新输入.\033[0m')
            continue
        if choice == '2':
            print('bye-bye')
            break
        cmds[choice]()


if __name__ == '__main__':
    show_menu()

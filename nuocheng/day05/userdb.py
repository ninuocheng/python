userdb = {}

def register():
    username = input('用户名: ').strip()
    if username:
        if username in userdb:
            print('用户已注册,请重新输入.')
        else:
            password = input('密码: ').strip()
            if password:
                userdb[username] = password
                print('用户注册成功.')
            else:
                print('密码不能为空.')

    else:
        print('输入为空,请重新输入.')


def login():
    username = input('用户名: ').strip()
    password = input('密码: ').strip()
    if username in userdb:
        if userdb[username] == password:
            print('登录成功.')
        else:
            print('登陆失败')
    else:
        print('登陆失败.')



def show_menu():
    cmds = {'0': register, '1': login}
    prompt = """(0) 注册
(1) 登录
(2) 退出
请选择(0/1/2): """
    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2']:
            print('\033[31;1m无效的输入,请重试.\033[0m')
            continue
        if choice == '2':
            print('\033[31;1mbye-bye\033[0m')
            break
        cmds[choice]()


if __name__ == '__main__':
    show_menu()
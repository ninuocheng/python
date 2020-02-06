stack = []


def push_it():
    data = input('数据: ').strip()
    if data:
        stack.append(data)
    else:
        print('\033[31;1m输入为空,请重新输入.\033[0m]')


def pop_it():
    if stack:
        print('从栈中弹出了: \033[34;1m%s\033[0m' % stack.pop())
    else:
        print('\033[31;1m空栈\033[0m')


def view_it():
    print('\033[31;1m%s\033[0m' % stack)


def show_menu():
    prompt = """(0): 压栈
(1): 出栈
(2): 查询
(3): 退出
请选择（0/1/2/3）:"""
    # 将各个函数保存到字典中
    cmds = {'0': push_it, '1': pop_it, '2': view_it}
    while 1:
        choice = input(prompt).strip()
        if choice not in ['0', '1', '2', '3']:
            print('\033[31;1m无效的参数,请重试.\033[0m')
            continue
        if choice == '3':
            print('\033[31;1mbye-bye\033[0m')
            break
        cmds[choice]()


if __name__ == '__main__':
    show_menu()

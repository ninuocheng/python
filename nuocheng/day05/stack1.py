stack = []


def push_it():
    data = input('数据: ').strip()
    if data:
        stack.append(data)
    else:
        print('\033[31;1m输入为空,请重试.\033[0m')


def pop_it():
    if stack:
        print('\033[31;1m从栈中弹出了: %s\033[0m' % stack.pop())
    else:
        print('空栈')

def view_it():
    print('\033[33;1m%s\033[0m' % stack)


def show_menu():
    prompt = """(0): 压栈
(1): 出栈
(2): 查询
(3): 退出
请选择（0/1/2/3）:"""
    while 1:
        prompt1 = input(prompt).strip()
        # if prompt1 == '':
        #     print('输入为空,请重新输入.')
        #     continue
        if prompt1 in str(list(range(4))):
            if prompt1 == '':
                print('\033[34;1m输入为空,请重新输入.\033[0m')
                continue

            # if type(int(prompt1)) == int:
            choice = int(prompt1)
            if choice in [0, 1, 2, 3]:
                if not choice:
                    push_it()
                elif choice == 1:
                    pop_it()
                elif choice == 2:
                    view_it()
                else:
                    print('bye-bye')
                    break
        else:
            print('\033[31;1m无效的参数,请重新输入.\033[0m')
        # else:
        #     print('无效的参数,请重新输入')
        #


if __name__ == '__main__':
    show_menu()

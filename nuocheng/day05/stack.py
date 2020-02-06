result = []


def yz():
    while 1:
        alist = input('数据:').strip()
        if not alist:
            print('\033[31;1m输入为空,请重新输入.\033[0m')
            continue
        result.append(alist)
        return result


def cz():
    if result:
        print('从栈中弹出了:', '\033[32;1m%s\033[0m' % result.pop())
        if result:
            print('从栈中弹出了: ' + '\033[33;1m%s\033[0m' % result.pop())
            if result:
                print('从栈中弹出了: \033[34;1m%s\033[0m' % result.pop())
    else:
        print('\033[31;1m空栈.\033[0m')


def cx():
    print('\033[31;1mresult\033[0m')
    print('\033[31;1m%s\033[0m' % result)


def show_menu():
    while 1:
        info = input("""(0) 压栈
(1) 出栈
(2) 查询
(3) 退出
请选择（0/1/2/3）:""").strip()
        if info not in ['0', '1', '2', '3']:
            print('无效的参数')
            continue
        if info == '0':
            yz()
        elif info == '1':
            cz()
        elif info == '2':
            cx()
        else:
            print('bye-bye')
            break


if __name__ == '__main__':
    show_menu()

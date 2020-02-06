s = '741852963789456123'
for ch in s:
    if ch not in '0123456789':
        print(False)
        break
        # print(1)
    # print(2)

else:   #break掉就不会执行else
    print(True)
print(True) # 循环结束都会执行
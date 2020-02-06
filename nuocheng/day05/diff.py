#修改mima2,使之与mima不一样
with open('/tmp/mima') as f1:
    aset = set(f1)
with open('/tmp/mima2') as f2:
    bset = set(f2)
with open('/tmp/result.txt', 'w') as f3:
    f3.writelines(bset - aset)   # bset中有aset中没有的行
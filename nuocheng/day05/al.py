import random
alist = [random.randint(1, 100) for i in range(5)]
print(alist)
alist[-1] = 21
alist[1:3] = [1, 3, 5, 7, 9]
print(alist)
alist.append(5)
print(alist)
alist.insert(0, 5)
print(alist)
print(alist.count(5))
print(alist.index(5))
alist.append([1, 2])
print(alist)
alist.extend([1, 2])
print(alist)
print(alist.pop())
print(alist.remove(5))
print(alist)
print(alist.pop(-2))
print(alist)
alist.reverse()
print(alist)
alist.sort() #默认升序排列
print(alist)
alist.sort(reverse=True) #降序排列
print(alist)
blist =alist.copy() #将alist的值赋值给blist,但采用不同内存空间
print(blist)
print(alist)
alist.reverse() #翻转
print(alist)
print(blist)
clist = alist
print(alist)
print(clist)
alist.reverse()
alist.append(100)
print(alist)
print(clist)
print(blist)
alist.clear() #清空列表
print(alist)
print(blist)
print(clist)
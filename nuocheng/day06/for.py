import time
result = 0
t1 = time.time()
for i in range(1, 10000000000001):
    result += i
t2 = time.time()
print(result)
t3 = t2 - t1
print(t3)

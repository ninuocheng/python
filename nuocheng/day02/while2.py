# result = 0
# counter = 0
# while counter < 100:
#     counter += 1
#     if counter % 2 == 1:
#         continue
#     else:
#         result += counter
# print(result)
# result = 0
# counter = 0
# while counter < 100:
#     counter += 1
#     if counter % 2:
#         continue
#     result += counter
# print(result)
result0 = 0
result1 = 0
counter = 0
while 1:
    counter += 1
    if counter % 2:
        result1 += counter
        continue
    result0 += counter
    if counter == 100:
        print(result0, result1)
        break
print(result0 + result1)
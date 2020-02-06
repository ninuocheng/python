# result = 0
# count = 1
# while count <= 100:
#     result += count
#     count += 1
# print(count)
# print(result)
# count = 1
# result = 1
# while count < 100:
#     count += 1
#     result += count
# print(count)
# print(result)
# import random
# choices = ['shitou', 'jiandao', 'bu']
# win_list = [['shitou', 'jiandao'], ['jiandao', 'bu'], ['bu', 'shitou']]
# prompt = '''(0): shitou
# (1): jiandao
# (2): bu
# please select(0/1/2): '''
# pwin = 0
# cwin = 0
# while pwin < 2 and cwin < 2:
#     computer = random.choice(choices)
#     index = int(input(prompt))
#     player = choices[index]
#     print("Your choice: %s, computer's choice: %s" % (player, computer))
#     if player == computer:
#         print('\033[32;1mping ju\033[0m')
#     elif [player, computer] in win_list:
#         pwin += 1
#         print('\033[31;1mYou win\033[0m')
#     else:
#         cwin += 1
#         print('\033[31;1mYou lose\033[0m')
import random
choices = ['shitou', 'jiandao', 'bu']
win_list = [['shitou', 'jiandao'], ['jiandao', 'bu'], ['bu', 'shitou']]
prompt = '''(0): shitou
    (1): jiandao
    (2): bu
    please select(0/1/2): '''
pwin = 0
cwin = 0
while 1:
    computer = random.choice(choices)
    index = int(input(prompt))
    player = choices[index]
    print("Your choice: %s, computer's choice: %s" % (player, computer))
    if player == computer:
        print('\033[32;1mping ju\033[0m')
    elif [player, computer] in win_list:
        pwin += 1
        print('\033[31;1mYou win\033[0m')
    else:
        cwin += 1
        print('\033[31;1mYou lose\033[0m')
    if pwin == 2 or cwin == 2:
        break
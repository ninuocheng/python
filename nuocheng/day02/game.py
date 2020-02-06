# import random
# computer = random.choice(['shi tou', 'jian dao', 'bu'])
# player = input('shi tou/jian dao/bu:')
# print("Player's choice is %s, Computer's choice is %s" % (player, computer))
# if player == 'shi tou':
#     if computer == 'shi tou':
#         print('ping ju')
#     elif computer == 'jian dao':
#         print('You win')
#     else:
#         print('You lose')
# elif player == 'jian dao':
#     if computer == 'shi tou':
#         print('You lose')
#     elif computer == 'jian dao':
#         print('ping ju')
#     else:
#         print('You win')
# else:
#     player == 'bu'
#     if computer == 'shi tou':
#         print('You win')
#     elif computer == 'jian dao':
#         print('You lose')
#     else:
# #         print('ping ju')
# import random
# choices = ['shitou', 'jiandao', 'bu']
# computer = random.choice(choices)
# player = input('please chu quan(shitou/jiandao/bu): ')
# print("Your choice is %s, computer's choice is %s" % (player, computer))
# if player == 'shitou':
#     if computer == 'shitou':
#         print('pingju')
#     elif computer == 'jiandao':
#         print('You win')
#     else:
#         print('You lose')
# elif player == 'jiandao':
#     if computer == 'shitou':
#         print('You lose')
#     elif computer == 'jiandao':
#         print('ping ju')
#     else:
#         print('You win')
# else:
#     if computer == 'shitou':
#         print('You win')
#     elif computer == 'jiandao':
#         print('You lose')
#     else:
#         print('ping ju')
# import random
# choices = ['shitou', 'jiandao', 'bu']
# win_list = [['shitou', 'jiandao'], ['jiandao', 'bu'], ['bu', 'shitou']]
# computer = random.choice(choices)
# player = input('please chu quan(shitou/jiandao/bu): ')
# print("Your choice: %s, computer's choice: %s" % (player, computer))
# if player == computer:
#     print('\033[32;1mping ju\033[0m')
# elif [player, computer] in win_list:
#     print('\033[31;1mYou win\033[0m')
# else:
#     print('\033[31;1mYou lose\033[0m')
import random
choices = ['shitou', 'jiandao', 'bu']
win_list = [['shitou', 'jiandao'], ['jiandao', 'bu'], ['bu', 'shitou']]
prompt = '''(0): shitou
(1): jiandao
(2): bu
please select(0/1/2): '''
computer = random.choice(choices)
index = int(input(prompt))
player = choices[index]
print("Your choice: %s, computer's choice: %s" % (player, computer))
if player == computer:
    print('\033[32;1mping ju\033[0m')
elif [player, computer] in win_list:
    print('\033[31;1mYou win\033[0m')
else:
    print('\033[31;1mYou lose\033[0m')
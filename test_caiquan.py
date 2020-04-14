import random

shitou = 0
jiandao = 1
bu = 2

# 使用input接收用户出的拳
player = input('请出拳 石头（0） 剪刀（1） 布（2） ：')
if int(player) == shitou:
    print('用户出的是 石头')
elif int(player) == jiandao:
    print('用户出的是 剪刀')
elif int(player) == bu:
    print('用户出的是 布')

# 使用随机函数生成电脑每次出的拳
computer = random.randint(0,2)
if int(computer) == shitou:
    print('电脑出的是 石头')
elif int(computer) == jiandao:
    print('电脑出的是 剪刀')
elif int(computer) == bu:
    print('电脑出的是 布')

if (int(player) == 0 and int(computer) == 1) or (int(player) == 1 and int(computer) == 2) or (int(player) == 2 and int(computer) == 0):
    print('玩家胜利！')
elif (int(player) == 0 and int(computer) == 2) or (int(player) == 1 and int(computer) == 0) or (int(player) == 2 and int(computer) == 1):
    print('电脑胜利！')
elif (int(player) == 0 and int(computer) == 0) or (int(player) == 1 and int(computer) == 1) or (int(player) == 2 and int(computer) == 2):
    print('两方平手！')
else:
    print('请玩家重新输入正确的值！')
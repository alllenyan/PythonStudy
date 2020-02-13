name1 = input('小精灵：您好，欢迎来到古灵阁，请问您需要帮助吗？需要or不需要？')
# input()函数可直接在控制台打印出函数内的内容，变量用于保存input接受的内容

if name1 == '需要':
    name2 = int(input('请问您需要什么帮助呢？1 存取款；2 货币兑换；3 咨询'))
    if name2 == 2:
            print('金加隆和人民币的兑换率为1:51.3，即一金加隆=51.3人民币')
            name3 = int(input('请问您需要兑换多少金加隆呢？'))
            print('好的，我知道了，您需要兑换' + str(name3) + '金加隆')
            print('那么，您需要付给我' + str(name3 * 51.3) + '人民币')

    elif name2 == 1:
            print('请去存取款窗口')

    else:
            print('请去咨询窗口')
else:
    print('好的，再见。')


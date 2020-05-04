# 尝试编写一个用户登录程序（这次尝试将功能封装成函数）
print('|--- 新建用户：N/n ---|')
print('|--- 登录账号：E/e ---|')
print('|--- 退出程序：Q/q ---|')

user = dict()


def logon():
    while True:
        username = input('请输入用户名:')
        if username not in user:
            print('输入的用户名在系统中不存在')
            continue
        else:
            password = input('请输入密码:')
            if password == user[username]:
                print('欢迎进入系统，请点击右上角结束程序！')
                break
            else:
                print('密码输入错误，登陆系统失败！')
                break


def zhuce():
    while True:
        username = input('请输入用户名:')
        if username in user:
            print('输入的用户名已存在于系统中，请重新输入')
            continue
        else:
            password = input('请输入密码:')
            user[username] = password
            return user
            break


while True:
    zhiling = input('请输入指令:')
    if zhiling == 'Q' or zhiling == 'q':
        break
    elif zhiling == 'N' or zhiling == 'n':
        zhuce()
    elif zhiling == 'E' or zhiling == 'e':
        logon()
    else:
        print('请输入正确的指令')

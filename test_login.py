i = 0
while True:
    username = input('请输入你的用户名:')
    password = input('请输入你的密码:')
    if username == 'zhangsan' and password == '123':
        print('账号密码输入正确，登陆成功！')
        break
    i = i + 1
    if i == 3:
        print('账号密码输入过多，账号已被锁定')
        break
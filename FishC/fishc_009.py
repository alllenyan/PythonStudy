# 设计一个验证用户密码程序，用户只有三次机会输入错误，不过如果用户输入的内容中包含"*"则不计算在内。
total = 0
while True:
    password = input('请输入密码:')
    if '*' in password:
        print('密码中不能含有*号')
        continue
    else:
        if password == 'mima':
            print('密码输入正确')
            break
        else:
            total += 1
            print('密码输入错误')
            if total == 3:
                print('输入次数达到最大限制')
                break

# 编写一个程序，求 100~999 之间的所有水仙花数。
# 如果一个 3 位数等于其各位数字的立方和，则称这个数为水仙花数。例如：153 = 1^3 + 5^3 + 3^3，因此 153 就是一个水仙花数。
x = 0
y = 0
z = 0
for i in range(100, 1000):
    x = i // 100
    y = i // 10 % 10
    z = i % 10
    if i == (x ** 3 + y ** 3 + z ** 3):
        print(i)

# 有红、黄、蓝三种颜色的球，其中红球 3 个，黄球 3 个，绿球 6 个。先将这 12 个球混合放在一个盒子中，
# 从中任意摸出 8 个球，编程计算摸出球的各种颜色搭配。
print('red\tyellow\tgreen')
for red in range(0, 4):
    for yellow in range(0, 4):
        for green in range(2, 7):
            if red + yellow + green == 8:
                print(red, '\t', yellow, '\t', green)

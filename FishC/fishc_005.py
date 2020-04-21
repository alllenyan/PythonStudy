# 输入一个年份，判断是否是闰年
while True:
    year = input('请输入一个年份:')
    if year.isdigit():
        if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
            print('这是一个闰年')
            break
        else:
            print('这不是一个闰年')
            break
    else:
        print('请输入一个正确的年份')

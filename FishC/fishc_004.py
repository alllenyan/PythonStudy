import random

# 让用户输入数字，与系统生成的比较，如果对了则提示用户猜测正确，否则告知用户猜大或猜小
total = 0
num2 = random.randint(1, 10)
print('系统生成的数字为:', num2)
while True:
    num1 = input('请输入一个1-10之内的数字：')
    if num1.isdigit():
        if int(num1) > num2:
            print('你输入的数字偏大')
        elif int(num1) == num2:
            print('你回答正确')
            break
        else:
            print('你输入的数字偏小')
        total += 1
        if total == 3:
            print('你的输入机会已经使用完毕')
            break
    else:
        # if num1 < 1 or num1 > 10:
        print('请输入一个符合要求的数字')

# 由用户输入一个数字，打印从1到用户输入的数字间所有的数字
num3 = int(input('请输入一个数字:'))
i = 0
while i < num3:
    i += 1
    print(i)

# 输入一个数字，根据用户输入的数字打印空格和星号
num4 = int(input('请输入一个数字:'))
while num4 > 0:
    print(' ' * (num4-1) + '*' * num4)
    num4 -= 1

#根据输入的百分制成绩判断及格还是不及格，60分以上为及格
score = int(input('输入考试的成绩:'))
if score < 60:
    print('成绩不及格！')
else:
    print('成绩及格！')

#根据输入的年龄判断这个人是否未成年，18岁以下为未成年，如果输入的数字大于150则输出这不是个人
age = int(input('请输入你的年龄:'))
if 0 < age < 18:
    print('你未成年！')
elif 18 <= age <= 150:
    print('你成年了！')
else:
    print('你不是个人！')

#输入两个数，两个数相减的结果如果为奇数则输出，否则输出"这不是奇数"
number1 = float(input('please enter a number:'))
number2 = float(input('please enter another number:'))
result = 0
if number1 > number2:
    result = number1 - number2
else:
    result = number2 - number1

if result % 2 == 0:
    print('这不是个奇数！')
else:
    print(result)

#使用for循环输出0到100之间的奇数
i = 0
for i in range(0,100):
    i = i + 1
    if i % 2 != 0:
        print(i)

#使用while循环输出0到100之间的偶数
j = 0
while j <= 100:
    j = j + 1
    if j % 2 == 0:
        print(j)

#用循环语句写出1到100间的数字和
t1 = 0
t2 = 0
for t1 in range(0,100):
    t1 = t1 + 1
    t2 = t2 + t1

print(t2)

#统计100以内个位数是2并且能否被三整除的数
t3 = 0
t4 = 0
for t3 in range(1,101):
    if t3 % 3 == 0 and t3 % 10 == 2:
        t4 = t4 + 1
        print(t3)
    t3 = t3 + 1
print(t4)

#输入一个正整数，求他是几位数
t5 = int(input('请输入一个正整数:'))
t6 = 0
t7 = 0
for t6 in range(1,101):
    t7 = t7 + 1
    t5 = t5 // 10
    if t5 == 0:
        break
print(t7)

#打印水仙花数，水仙花数是一个三位数，其各位数立方和等于该数本身
t8 = 0
for t8 in range(100,1000):
    x = t8 // 100
    y = t8 % 100 // 10
    z = t8 % 10
    if t8 == (x**3 + y**3 + z**3):
        print(t8)

#统计101-200之间的所有素数及其个数
t9 = 0
t10 = 0
t11 = 0
for t9 in range(101,201):
    for t10 in range(2,t9):
        if t9 % t10 == 0:
            break
    else:
        print(t9)
        t11 = t11 + 1
print('质数的个数为:',t11)
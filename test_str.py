a = '''xiaoming shuo:"ta shi xiaoming"'''
b = 'xiaoming shuo:\"ta shi xiaoming\"'

print(a)
print(b)


def foo(str):
    print(str)


# str = input('请输入你要说的话:')
# foo(str)


# 输入两个数，计算这两个数的最小公约数和最小公倍数
def math1(x, y):
    (x, y) = (y, x) if x < y else (x, y)
    for i in range(1, y):
        if x % i == 0 and y % i == 0:
            return i
    else:
        return '无最小公约数'


def math2(x, y):
    return x * y

num1 = input('请输入数字1:')
num2 = input('请输入数字2:')
print('两个数的最小公约数为：',math1(num1,num2))
print('两个数的最小公倍数为：',math2(num1,num2))

# 0. 编写一个函数 power() 模拟内建函数 pow()，即 power(x, y) 为计算并返回 x 的 y 次幂的值。
# 1. 编写一个函数，利用欧几里得算法（脑补链接）求最大公约数，例如 gcd(x, y) 返回值为参数 x 和参数 y 的最大公约数。

def power(x, y):
    print(x ** y)


def gongyueshu(x, y):
    for i in range(1,100):
        if x % i == 0 and y % i == 0:
            print('最大公约数为', i)

def gcd(x, y):
    while y:
        t = x % y
        x = y
        y = t

    return x

power(2, 2)
gongyueshu(4, 6)
print(gcd(4,6))

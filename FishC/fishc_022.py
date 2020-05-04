#  请使用lambda表达式将下边函数转变为匿名函数？
# def fun_A(x, y=3):
#         return x * y

niminghanshu = lambda x, y=3: x * y
print(niminghanshu(2))


# 1. 请将下边的匿名函数转变为普通的屌丝函数？
# lambda x : x if x % 2 else None
def hanshu1(x):
    if x % 2 == 0:
        return x
    else:
        return None


print(hanshu1(4))

# 3. 你可以利用 filter() 和 lambda 表达式快速求出 100 以内所有 3 的倍数吗？

list1 = list(filter(lambda x: not (x % 3), range(1, 101)))
print(list1)

# 使用递归编写一个 power() 函数模拟内建函数 pow()，即 power(x, y) 为计算并返回 x 的 y 次幂的值

# 闭包概念理解
def outterFun(x):
    def innerFun(y):
        return x * y

    return innerFun


a = outterFun(3)
print(a)
print(a(2))

# 作用域的个人理解联系
# 定义在最外层的变量为全局变量，在函数中可以读取到全局变量
# 定义在函数内的变量为局部变量，局部变量在函数外部不可以访问
# 当全局变量与函数内的局部变量变量名相同时，调用函数输入全局变量之后，函数优先使用函数内的局部变量
# 函数的参数也是全局变量
a = 10


def cal(a):
    a = 5
    b = a ** 2
    print(b)


cal(a)
# print(b) 变量b不可以在函数外访问

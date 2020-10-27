# name = input('请输入你的姓名:')
# print('你好' + name)
#
# number = int(input('请输入1到100之间的数字:'))
# if 1 < number < 100:
#     print('你妹好漂亮')
# else:
#     print('你大爷好丑')

def playx(x):
    print("playx函数调用，x的值是{0}".format(x))
    def playy(y):
        print("playy函数调用，y的值是{0}".format(y))
        return x * y
    return playy

result = playx(5)
result2 = result(8)
print(result2)

str1 = "阿迪斯,发士大,夫的发,生发射点,发射点,发射点"

str2 = str1.split(",")

str3 = str1.split(",",2)

print(str2)
print(str3)

try:
    print(str4)
except NameError as reason:
    print("变量名未定义导致的错误" + str(reason))
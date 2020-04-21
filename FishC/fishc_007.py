# 根据输入的分数判断该分数所处的等级
score = input('请输入你的分数:')
if score.isdigit():
    if 100 >= int(score) >= 90:
        print('A')
    elif 80 <= int(score) < 90:
        print('B')
    elif 60 <= int(score) < 80:
        print('C')
    elif 100 < int(score):
        print('输入的分数不合法')
    else:
        print('D')
else:
    print('输入的分数不合法')

# # 使用三元表达式将xyz中最小的值赋予small变量
# x, y, z = 6, 5, 4
# small = 0
# samll = y if x > y else small = x


for i in range(1,11,2):
    print(i)
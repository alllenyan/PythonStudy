# 打印*矩阵
j = 0
while j < 5:
    j = j + 1
    i = 0
    while i < 5:
        i = i + 1
        print('*', end=' ')
    print()

# 打印*三角形
j = 0
while j < 5:
    j = j + 1
    i = 0
    while i < j:
        i = i + 1
        print('*', end=' ')
    print()

# 打印9*9乘法表
j = 0
while j < 9:
    j = j + 1
    i = 0
    while i < j:
        i = i + 1
        print(i, '*', j, '=', i * j, end=' ')
    print()

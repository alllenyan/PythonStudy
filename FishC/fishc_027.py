# 0. 编写一个程序，接受用户的输入并保存为新的文件
def readFile(filename):
    f = open(filename, 'w')

    print("请输入内容[单独输入':w'保存退出]")

    while True:
        content = input()
        if content != ':w':
            f.write(content + '\n')
        else:
            break

    f.close()


filename = input('请输入文件名:')
filename = 'c:\AllenYan\learn\\' + filename
readFile(filename)

# 编写一个程序，比较用户输入的两个文件，如果不同，显示出所有不同处的行号与第一个不同字符的位置
def getFile(filename):
    filename = 'c:\AllenYan\learn\\' + filename
    f = open(filename)
    file_content = []

    for line in f:
        file_content.append(line)

    f.close()

    return file_content


def compareFiles(filename1, filename2):
    length1 = len(filename1)
    length2 = len(filename2)
    longlength = 0
    hanghao = []
    count = 0

    if length1 > length2:
        longlength = length2
    else:
        longlength = length1

    for i in range(0, longlength - 1):
        if filename1[i] != filename2[i]:
            hanghao.append(i)
            count += 1

    return (count, hanghao)


file1 = input('请输入需要比较的第一个文件:')
file2 = input('请输入需要比较的第二个文件:')

count, hanghao = compareFiles(getFile(file1), getFile(file2))

print('两个文件共有' + str(count) + '处不同:')

for i in hanghao:
    print('第' + str(hanghao[i]) + '行不一样')

# 编写一个程序，当用户输入文件名和行数（N）后，将该文件的前N行内容打印到屏幕上
filename3 = open('c:\AllenYan\learn\\record.txt')

number = int(input('请输入需要显示该文件的前几行:'))

for i in range(0,number):
    print(filename3.readline())

filename3.close()

# 编写一个程序，实现“全部替换”功能，程序实现如图
def replaceFile(filename, replacestr1, replacestr2):
    filename = 'c:\AllenYan\learn\\' + filename
    content = []

    f = open(filename)

    for line in f:
        content.append(line)

    for i in range(0, len(content)):
        if replacestr1 in content[i]:
            content[i] = content[i].replace(replacestr1, replacestr2)

    f.close()

    filename1 = 'c:\AllenYan\learn\\666.txt'

    filename1_content = open(filename1, 'a')

    filename1_content.writelines(content)

    filename1_content.close()


filename = input('请输入文件名:')
replace1 = input('请输入需要替换的单词或字符:')
replace2 = input('请输入新的单词或字符:')

replaceFile(filename, replace1, replace2)

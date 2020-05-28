import os
# 0. 编写一个程序，统计当前目录下每个文件类型的文件数
py = 0
txt = 0
png = 0
jpg = 0
houzhui = dict()
daxiao = dict()

lujing = 'c:\\AllenYan\learn'

content = os.listdir(path=lujing)

for i in range(0,len(content)):
    if content[i].split('.')[1] == 'py':
        py += 1
    elif content[i].split('.')[1] == 'txt':
        txt += 1
    elif content[i].split('.')[1] == 'png':
        png +=1
    else:
        jpg+=1

houzhui['.py'] = py
houzhui['.txt'] = txt
houzhui['.png'] = png
houzhui['.jpg'] = jpg

print(houzhui)

# 1. 编写一个程序，计算当前文件夹下所有文件的大小

for i in range(0,len(content)):
    daxiao[content[i]] = os.path.getsize(lujing+'\\'+content[i])

print(daxiao)

# 2. 编写一个程序，用户输入文件名以及开始搜索的路径，搜索该文件是否存在。如遇到文件夹，则进入文件夹继续搜索

while True:
    if os.path.isdir(lujing):
        print('wenjianjia')
        break
    elif os.path.isfile(lujing):
        print('wenjian')
        break
    else:
        print('wrong')
        break
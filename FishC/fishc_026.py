f = open('c:\AllenYan\learn\\record.txt')

boy_content = []
girl_content =[]
count = 1

for i in f:
    if i[:6] != '======':
        role,content = i.split(':',1)
        if role == '小甲鱼':
            boy_content.append(content)
        if role == '小客服':
            girl_content.append(content)
    else:
        boy_file_name = 'c:\AllenYan\learn\\boy_'+str(count)+'.txt'
        girl_file_name = 'c:\AllenYan\learn\\girl_'+str(count)+'.txt'

        boy = open(boy_file_name,'w')
        girl = open(girl_file_name,'w')

        boy.writelines(boy_content)
        girl.writelines(girl_content)

        boy.close()
        girl.close()

        boy_content = []
        girl_content = []
        count += 1

boy_file_name = 'c:\AllenYan\learn\\boy_'+str(count)+'.txt'
girl_file_name = 'c:\AllenYan\learn\\girl_'+str(count)+'.txt'

boy = open(boy_file_name,'w')
girl = open(girl_file_name,'w')

boy.writelines(boy_content)
girl.writelines(girl_content)

boy.close()
girl.close()

boy_content = []
girl_content = []
count += 1

f.close()
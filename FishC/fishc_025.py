f = open('C:\AllenYan\learn\OpenMe.mp3')
file_content = []
for i in f:
    file_content.append(i)

f.close()

print(file_content)

f1 = open('C:\AllenYan\learn\OpenMe.txt', 'a')
f1.writelines(file_content)
f1.close()

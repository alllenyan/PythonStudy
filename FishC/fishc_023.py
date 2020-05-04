# 尝试利用字典的特性编写一个通讯录程序吧
print('|--- 欢迎进入通讯录程序 ---|')
print('|--- 1.查询联系人资料 ---|')
print('|--- 2.插入新的联系人 ---|')
print('|--- 3.删除已有的联系人 ---|')
print('|--- 4.退出通讯录程序 ---|')
tongxunlu = {'allen': '123123123'}


def querytel():
    name = input('请输入联系人姓名：')
    print('查询的联系人的电话为：', tongxunlu.get(name))


def modifytel():
    name = input('请输入联系人姓名：')
    if name in tongxunlu:
        print('输入的联系人已经存在')
        panduan = input('是否修改用户资料：')
        if panduan == 'YES':
            telphone = input('请输入用户联系电话：')
            tongxunlu[name] = telphone
            return tongxunlu
        else:
            pass
    else:
        telphone = input('请输入联系人电话：')
        tongxunlu[name] = telphone
        return tongxunlu


def deltel():
    name = input('请输入联系人姓名：')
    tongxunlu.pop(name)
    return tongxunlu


while True:
    zhiling = int(input('请输入相关的指令代码:'))
    if zhiling == 1:
        querytel()
    elif zhiling == 2:
        modifytel()
    elif zhiling == 3:
        deltel()
    else:
        print('|--- 感谢使用通讯录程序 ---|')
        break

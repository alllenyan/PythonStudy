# 定义字典
a = {"a1":"a10","a2":"a20","a3":"a40","a5":"a60","a7":"a70","a8":"a80","a9":"a90"}
b = 0
c = a.keys()

for i in c:
    print("key:"+i+" values:"+a[i])


a1= {}
for i in range(0,10):
     a1[i] = 100

print(a1)

name = 'allen'
gender = 'male'
a1[name] = gender

print(a1)

b = "spr1/spr2/spr3"
b1 = b.split("/")
print(len(b1))

c = "spr1"
c1 = c.split("/")
print(c1)
print((len(c1)))
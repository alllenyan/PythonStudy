class Person:

    def __init__(self,name):
        self.name = name

    def getName(self):
        return self.name


class Person2:

    name = '123123'

    def setName(self,a):
        name = a
        return name

    def getName(self):
        return self.name

a = Person("jack")
b = Person2()
b.setName("mary")

print(a.getName())
print(b.name)
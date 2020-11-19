#OOP

class MyClass:
    #class object atributes
    menbership = True
    #atributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #methods
    def run(self):
        print('run')
        return 3


player1 = MyClass('seba','45')

print(player1.run())
print(player1.age)
# help(MyClass)
print(player1.menbership)
print(dir(MyClass))
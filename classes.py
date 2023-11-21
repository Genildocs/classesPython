class Calculator():
    def add(self, x, y):
        return x + y
    def sub(self, x, y):
        return x - y
    def mult(self, x, y):
        return x * y
    def div(self, x, y):
        if(y == 0):
            return "Cannot divide by zero"
        return x / y
calc = Calculator()

print(calc.div(10, 5))
print(calc.mult(12, 5))
print(calc.sub(10, 5))
print(calc.add(10, 5))

print(2 * '--------------------------------')
print(2 * '--------------------------------')
class Player():
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def get_age(self):
        return f'{self.name} is age {self.age}'
    def get_height(self):
        return f'{self.name} is {self.height} cm tall'
    def get_weight(self):
        return f'{self.name} is {self.weight} kg heavy'

p1 = Player("Genildo",  30, 1.65, 95)
p2 = Player('Lionel', 35, 1.75, 100)
print(p1.name)
print(p2.name)
print(p1.get_age(), p1.get_height(), p1.get_weight())
print(p2.get_age(), p2.get_height(), p2.get_weight())
print(2 * '--------------------------------')
print(2 * '--------------------------------')

class Name():
    def fname(self, fname):
        return fname.capitalize()
    def lname(self, lname):
        return lname.capitalize()
    def fullname(self, fname, lname):
        return f'{fname.capitalize()} {lname.capitalize()}'
    def initials(self, fname, lname):
        return f'{fname[0].capitalize()}.{lname[0].capitalize()}'



name2 = Name()
print(name2.fname('george'))
print(name2.lname('martin'))
print(name2.fullname('george', 'martin'))
print(name2.initials('george', 'martin'))

print(2 * '--------------------------------')
print(2 * '--------------------------------')


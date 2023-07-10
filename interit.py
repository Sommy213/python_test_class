class Animal:
    def __init__(self,name):
        self.name = name
    def sound (self):
        print('animal sound')
    def __init__(self,name):
        Animal.__init__(self,name)
        
class Dog (Animal):
    def eat (self):
        print('eating')
puppy = Dog()
puppy.eat()
puppy.sound()
# lclass child (f
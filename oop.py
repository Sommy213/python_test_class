class Animal:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
    def sound (self):
        if self.name =='cat':
            print('meow')
        elif self.name =='dog':
             print('bark')
           
        else:
           print("Do not sound")
    def get_profile(self):
        print(f"the {self.name} is a self {self.gender} and it  age {self.age} years old")
    def profile(self):
        self.get_profile()

dog = Animal("dog","male",12)
dog.age=24

dog.profile()

# print(dog.name)
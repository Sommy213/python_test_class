# name= len({'john', 'james'})
# print(name)
class Orangination:
    def __init__(self,org_name):
        self.org_name= org_name
class Employee1 (Orangination):
    def __init__(self, ename ,org_name):
       Orangination.__init__(self,org_name)
       self.employee =ename
class Employee2 (Orangination):
    def __init__(self, ename ,org_name):
       Orangination.__init__(self,org_name)
       self.employee =ename
class Manger (Employee1,Employee2):
    def __init__(self, ename1, ename2 ,org_name):
        Employee2.__init__(self,ename2,"FIRS")
        Employee2.__init__(self,ename1,org_name)
james = Manger("john","Alex","NNPC")
print(james.org_name)
# class pol
# class Manger:
#     def __init__(self,name,salary)
#         self.name = name
#         self.salary =salary
#     def profile(self):
#         return f"{self.name} get paid${self.salary}"
# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
#     def profile (self):
#         return f"{self.name} get paid${self.salary}"
#     john = Manger("john",200)
#     # noy funished
    
        


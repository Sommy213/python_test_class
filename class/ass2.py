class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary =salary
    def get_salary(self):
        return f"{self.name} get paid${self.salary}"
class Employee1 (Manger):
    def __init__(self, mname ,salary):
        Employee.__init__(self,salary)
        self.employee =mname
class Employee2 (Engineer):
    def __init__(self, ename ,salary):
       Employee.__init__(self,salary)
       self.employee =ename
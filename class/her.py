class Company:
    def __init__(self,company_name):
        self.company = company_name
    def profile(self):
        print(self.company)
class Employeee(Company):
    def __init__(self, name,company_name):
        super().__init__(company_name)
        self.name = name
        self.salary =50000
        
class Manager(Company):
    def __init__(self, name,company_name):
        super().__init__(company_name)
        self.name = name
        self.salary =10000000
class CheifExcutive(Company):
    def __init__(self, name,company_name):
        super().__init__(company_name)
        self.name=name
        self.salary = 100000
john = Employeee("John","First")
James = Manger("james", "First")
Jams = Manger("jams", "First")
Jack = CheifExcutive("jack", "First")
Jack.name = "jack"
Jack.profile()


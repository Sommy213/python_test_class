class Company:
    def __init__(self,company_name):
        self.company = company_name
    def profile(self):
        print(self.company)

class Work(Company):
    def __init__(self, ocupation,company):
        super().__init__(company)
        self.ocupation=ocupation
    def work_profile(self):
        print(f"The company (self.company)has (self.occupation)")




class Employee(Work):
    def __init__(self,salary,name, company,work):
        super().__init__(work,company)
        self.ename =name
        self.salary = salary
    def staff_profile(self):
        print(f"(self.name) works in (self.company) as (self.ocupation)") 
john = Employee(1000, "john", "FIRST","tech_Engineer") 
print(john.company)           
                
                

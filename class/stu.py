class Grades:
    def __init__(self, name,score):
        self.name = name
        self.score = score
    def result(self):   
        if self.score >= 70 :
            print("A")
        elif self.score  >= 60:
            print("B")
        elif self.score  >= 50:
            print("C")
        elif self.score  >= 30:
            print("E")
        else:
            print("f") 
    def __str__(self):
        return self.name
            



with open ('name.txt','r')as file :
    results = file.readlines()
    
grades = []
for data in results:
   data = data.split(',')
   grades.append(Grades(data[0], int(data[1].strip('\n'))))
            
        
for grade in grades:
    grade.result()
        
    
    
        
        
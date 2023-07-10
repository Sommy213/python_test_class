
class Grades:
    def __init__(self, result):    
        self.result = result
       
    def scores (self):
        for i in self.result: 
        
            if self.result[i]  >= 70 :
                print("A")
            elif self.result[i]  >= 69 & self.student <= 50:
                print("B")
            elif self.result[i]  >= 49 & self.student <= 30:
                print("C")
            elif self.result[i]  >= 29 & self.student <= 10:
                print("F")
            else:
                print(" you did not submit") 


grades = Grades({"chisom" :20, "victor":70, "gilly":59})
# grades.result()
print(grades.result)
print(len(grades.result))
class Student():
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def __str__(self) -> str:
            return self.id,self.name
class StudentRecordManger():
    def __init__ (self):
        self.students={}
    def add_student(self,stuid,name,score):
        if stuid in self.students:
            print(f'students{stuid}exits')
            return
        self.students[stuid]={'name':name,score :score}
    def view_student(self, stuid):
        if stuid not in self.students:
            print(f"Student {stuid} does not exist.")
            return
        print(f"ID: {stuid}, Name: {self.students[stuid]['name']}, score: {self.students[stuid]['sxcore']}")
    def update_student(self,stuid, name=None, score=None):
        if id not in self.students:
            print(f"Student {stuid} does not exist.")
            return
        if name is not None:
            self.students[stuid]['name'] = name
        if score is not None:
            self.students[stuid]['stuid'] = score
    def delete_student(self, id):
        if id not in self.students:
            print(f"Student {id} does not exist.")
            return
        del self.students[id]  
    
with open ('student.txt','r')as file :
    name = file.readlines()

for data in name:
   data = data.split(',')
   


print(name)
   
   






# class StudentManagementSystem:
#     def __init__(self):
#         self.students = {}

#     def add_student(self, id, name, grade):
#         if id in self.students:
#             print(f"Student {id} already exists.")
#             return
#         self.students[id] = {'name': name, 'score': grade}

#     def view_student(self, id):
#         if id not in self.students:
#             print(f"Student {id} does not exist.")
#             return
#         print(f"ID: {id}, Name: {self.students[id]['name']}, score: {self.students[id]['score']}")

#     def update_student(self, id, name=None, score=None):
#         if id not in self.students:
#             print(f"Student {id} does not exist.")
#             return
#         if name is not None:
#             self.students[id]['name'] = name
#         if grade is not None:
#             self.students[id]['score'] = score

#     def delete_student(self, id):
#         if id not in self.students:
#             print(f"Student {id} does not exist.")
#             return
#         del self.students[id]

# if __name__ == "__main__":
#     sms = StudentManagementSystem()
#     while True:
#         print("\n1. Add Student")
#         print("2. View Student")
#         print("3. Update Student")
#         print("4. Delete Student")
#         print("5. Quit")

#         response = int(input("Enter your choice: "))
#         if response== 1:
#             id = input("Enter student ID: ")
#             name = input("Enter student Name: ")
#             score = input("Enter student Grade: ")
#             sms.add_student(id, name, score)
#         elif response == 2:
#             id = input("Enter student ID: ")
#             sms.view_student(id)
#         elif response == 3:
#             id = input("Enter student ID: ")
#             name = input("Enter new student Name (leave blank if no change): ")
#             score = input("Enter new student Grade (leave blank if no change): ")
#             sms.update_student(id, name or None, score or None)
#         elif response == 4:
#             id = input("Enter student ID to delete: ")
#             sms.delete_student(id)
#         elif response == 5:
#             break
#         else:
#             print("Invalid choice. Please try again.")

    

            
        

 
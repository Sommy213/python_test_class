
class User:
    def __init__(self,name):
        self.name =name
    def __str__(self) -> str:
         return self.name
def main():
    all_attendence = []
   
    while True:
        
        print('1. Add an new student')
        print('2. mark attendence for a student')
        print('3. view  attendence for a student')
        print('4. generate attendence report')
        print('5. exit the program')
        response=input('')
        if response =='1':
           name = input('You are welcome enter your name please:')
           name = User(name)
           all_attendence.append(name)
           print('you are added')
           
        elif response=='2':
            name = input('enter your name:')
            for date in all_attendence:
                if date in all_attendence:
                   date =(input('enter the date:'))
                   print ('present welcome')
                   break
            else:
                print('absent')
                
        elif response =='3':
            for i in all_attendence:
                if i in all_attendence:
                    print(f'{name} is present in {date}')
                    
        elif response =='4':

            for i in  all_attendence:
                if i in all_attendence:
                    print(f'{name} attended the class on {date}')
                else:
                    print('Exit the program')
        else:
          print('Exit the program')
main()
                
            
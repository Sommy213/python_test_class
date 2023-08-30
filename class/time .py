from datetime import datetime
import time


def mark_attendence():


    while True:
        student=input('Enter the student name:')
        time_str = input('Enter the time,(format: HH:MM AM/PM): ')
        student_come =datetime.strftime(time_str, "%I:%M %p")
        ten_am =datetime.strptime('10:00AM','%I:%M %p')
        if student_come>ten_am:
            print('Absent')
        else:
            print('present')

mark_attendence()
            
        





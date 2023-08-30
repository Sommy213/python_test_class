import datetime
import mysql.connector as sql
from dotenv import load_dotenv
import os

load_dotenv()

db = sql.connect(
    host ='localhost',
    user='root',
    password='sommy213####',
    database='StudentRecord'
    )
cursor = db.cursor()

user = os.environ.get('user')
password = os.environ.get('sommy213####')
host = os.environ.get('host')


class StudentNotFound(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class Student:

    def __init__(self, id, first_name, last_name, phoneNumber):
        self.id = id
   
        self.first_name = first_name
        self.last_name = last_name
        self.phoneNumber = phoneNumber
        self.early = True

    def __str__(self) -> str:
        return self.name

class DB:
    def __init__(self) -> None:
        self.__db = sql.connect(
            host ='localhost',
            user='root',
            password='sommy213####',
            database='StudentRecord'
            )
        self.studentT = 'student'
        self.presentT = 'present'
        self.__cursor = self.__db.cursor()

    def add_new_student(self, student: Student):
        self.__cursor.execute(f'INSERT INTO {self.presentT} (FirstName, LastName, PhoneNumber) VALUES (%s, %s, %s)', (student.FirstName, student.LastName, student.PhoneNumber))      
        self.__db.commit()
    def update_student(self,firstName,id):
        self.__cursor.execute(f'UPDATE {self.presentT} SET FirstName = "{firstName}" WHERE id = {id}')
        self.__db.commit()
        
    def all_student(self):
        self.__cursor.execute(f'SELECT * FROM {self.student}')
        return self.__cursor.fetchall()
    
  
    




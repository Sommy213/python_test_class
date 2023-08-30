import random
# #from math import
# print(math.sqrt(2))
# import os
# print(os.chdir("C:\\Users\pc\Desktop\\new_app"))
# # print(os.listdir(""))
# os.name
# import random
# import time
# names =['john','james']
# time.sleep(5)
# print(random.choice(names))

def generatePassword():

    num = str(random.randrange(0,9))
    lower_case ='abcdefghijklm'
    upper_case ='lower_case.upper'
    special_charater='erwjnm'
    password = []
    for _ in range(10):
        
        our_choice =[random.choice(special_charater),str(random.randrange(0,9)),random.choice(lower_case),random.choice(upper_case)]
        password.append(random.choice(our_choice))
    return ''.join(password)
print(generatePassword())

with open('standaed_lab.txt','w+')as file:
    file.write(generatePassword())
    


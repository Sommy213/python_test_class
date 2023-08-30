
class User:
    def __init__(self,name,num):
        self.name =name
        self.num =num
    def __str__(self) -> str:
         return self.name
class Group:
    def __init__(self,title)-> None:
        self.title =title
        self.users =[]
    def add_user(self,user:User):
        self.users.append(user)
    def __str__(self) -> str:
        return self.title
class Attendence:
    def __init__(self) -> None:
        self.groups =[]
    def add_group(self,group:Group):
        self.groups.append(group)
        print(f"{group} has been added")
    def add_user_to_group(self,group:Group,user:User):
        if len(self.groups) !=0:
            for i in self.groups:
                if i == group:
                    i.add_user(user)
                    return f"{user} has been added to the {group}"
            else:
                return 'Could no find group'
        else:
            return 'No group added to the attendence' 
    def dispaly_all_groups(self):
        for group in self.groups:
            print(group)
    
    
        
    

if __name__ == '__main__':
    group1 = Group('Python Class')
    group2 = Group('Java Class')
    group3 = Group('ruby class')
    group4 = Group('Dart Class')
    group5 = Group("C class")
    attendence = Attendence()
    attendence.add_group(group1)
    attendence.add_group(group2)
    user1 = User('john',98038294293)
    user2 = User('jane',89034512784)
    user3 = User('james',99034512784)
    user8 = User('vicky',79034512784)
    user4 = User('queen',49034512784)
    user5 = User('jan',39034512784)
    user27 = User('timithy',39034512784)
    response = attendence.add_user_to_group(group1,user2)
    response2 = attendence.add_user_to_group(group1,user2)
    response3 = attendence.add_user_to_group(group3,user3)
    response4 = attendence.add_user_to_group(group1,user8)
    print(user1)
    print(response)
    print(response2)
         
          
        
    

        
       
   
		  
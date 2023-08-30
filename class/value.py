class Value:
    def __init__(self,num):
        self.num = num
    def __add__(self,val):
        return self.num +val.num
    def __sum__ (self):
        return self.num
a= Value(10)
b =Value(20)

c= a+b
print(c)
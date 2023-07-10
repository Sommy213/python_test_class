class Rectangle:
    def __init__(self,lenght,breadth):
        self.length =lenght
        self.breadth =breadth
    def display(self):
        print("Enter the the length of a reactangle is:", self.length)
        print("Enter the the breadth of a reactangle is:", self.breadth)
    def area(self):
        return (self.length*self.breadth)
    def per(self):
        return(2*self.length + 2*self.breadth)
l = int(input("Enter the length:"))
b = int(input("Enter the breadth:"))
r1= Rectangle(l,b)
print(r1.length)
print("retangle object:")
r1.display()
print("")
print("Area  of rectangle:",r1.area())

print("")
print("per of a rectangle is:",r1.per())


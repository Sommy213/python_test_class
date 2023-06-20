# import turtle
# import colorsys
# t=turtle.Turtle()
# s =turtle.Screen().bgcolor('black')
# t.speed(0)
# n=70
# h=90
# for i in range (360):
#     c=colorsys.hsv_to_rgb(1,2,3)
#     h+= 1/n
#     t.color(c)
#     t.left(2)
#     t.fd(1)
#     for j in range (1):
#         t.left(3)
#         t.circle(14)
import turtle
turtle.bgcolor('black')
squary = turtle.Turtle()
squary.speed(20)
squary.pencolor('red')
for i in range(480):
    squary.forward(i)
    squary.left(91)
    


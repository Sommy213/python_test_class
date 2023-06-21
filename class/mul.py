import turtle as tur
import colorsys as cs
from random import uniform
tur.bgcolor("black")
tur.speed(0)
for i in range (360):
    tur.color(cs.hsv_to_rgb(1/45,uniform(0,1),1))
    tur.pensize(2)
    tur.forward(150)
    tur.right(30)
    tur.forward(60)
    tur.left(90)
    tur.forward(60)
    tur.right(60)
    tur.penup()
    tur.setposition(0,0)
    tur.pendown()
    tur.right(1)
    
    tur.done()
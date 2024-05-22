#CODE = #B002
import turtle
n=turtle.Turtle ()
b=turtle.Screen()
b.bgcolor ('black')
n.width(3)
n.speed(25)
col=('magenta','yellow','green')
for y in range (500):
   n.pencolor(col[y%3])
   n.forward(y*4)
   n.right(121)
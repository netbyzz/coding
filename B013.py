#CODE = #B013
import colorsys
import turtle

t = turtle.Turtle()
e = turtle.Screen()

e.bgcolor('black')
t.speed(0)

b = 36
n = 0

for y in range (460):
    c = colorsys.hsv_to_rgb(n,1,0.8)
    n+=1/b
    t.color(c)
    t.left(145)

    for z in range (5):
        t.forward(300)
        t.left(150)
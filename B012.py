#CODE = #B012
from turtle import *
from colorsys import *
bgcolor('black')
tracer (100)
pensize(4)
n = 0

def draw(ang, b):
    circle(5+b, 60)
    left (ang)
    circle(5+2*b, 60)

goto(0,0)

for y in range(500):
    e = hsv_to_rgb(n,1,1)
    n += 0.005
    color(e)
    up()
    draw(90, y)
    draw(180, y)
    down()
    draw(1/2, y-y)
    draw(180, y/1)
    draw(120, y-1)
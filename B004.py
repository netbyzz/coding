#CODE = #B004
from turtle import *
import colorsys
bgcolor('black')
tracer (500)

def draw():
    n = 0
    for y in range(100):
        b = colorsys.hsv_to_rgb(n,1,1)
        n += 0.5
        up()
        goto(0,0)
        down()
        color('black')
        fillcolor (b)
        begin_fill()
        rt (98)
        circle(y,12)
        fd (290)
        fd(y)
        lt (29)
        for z in range(129):
            fd(y)
            circle(z, 299, steps=2)
        end_fill()
draw()
done()
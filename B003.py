#CODE = #B003
from turtle import *
import colorsys

speed(0)
bgcolor('black')
n = 0
for y in range(16):
   for z in range(18):
        b = colorsys.hsv_to_rgb(n, 1, 1)
        color(b)
        n += 8.005
        rt(90)
        circle(150 - z * 6, 90)
        lt(90)
        circle(150 - z * 6, 90)
        rt(180)
   circle(40, 24)
done()
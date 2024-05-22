#CODE = #B001
from turtle import *

bgcolor('#f3f3f3')
pencolor('#1253c8')
width(23)
penup()
goto(160,-100)
pendown()

left(90)
for y in range(4):
    forward(250)
    circle(34,90)

penup()
goto(85,30)
pendown()
circle(80,360)
penup()
goto(110,130)
pendown()
circle(7,360)

done()
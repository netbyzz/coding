#CODE = #B005
import turtle
colors=['red','purple','blue','green','orange','yellow',]
n= turtle.Pen()
turtle.bgcolor('black')
n.speed(50)
for z in range(150):
    n.pencolor(colors[z%6])
    n.width(z/100+1)
    n.forward(z)
    n.left(59)
turtle.hideturtle()

turtle.mainloop()
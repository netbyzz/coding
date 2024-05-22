#CODE = #B009
import turtle

def draw_attractive_design4():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(10)
    turtle.bgcolor("black")  
    pen.pensize(2)

    size = 20

    for y in range(300):
        pen.color(colors[y % 6])
        pen.forward(size)
        pen.left(59)
        pen.forward(size)
        pen.left(59)
        pen.forward(size)
        pen.left(59)
        pen.forward(size)
        pen.left(121)
        size += 2  

    pen.hideturtle()


draw_attractive_design4()

turtle.done()
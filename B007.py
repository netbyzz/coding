#CODE = #B007
import turtle

def draw_attractive_design1():
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    pen = turtle.Turtle()
    pen.speed(10)
    turtle.bgcolor("black")  
    pen.pensize(2)

    for y in range(180):
        pen.color(colors[y % 6])
        pen.forward(200)
        pen.right(61)
        pen.forward(100)
        pen.right(120)
        pen.forward(100)
        pen.right(61)
        pen.forward(200)
        pen.right(181)
        
    pen.hideturtle()

draw_attractive_design1()

turtle.done()
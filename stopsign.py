import turtle

sides = 8
length = 200
angle = 360/sides

turtle.penup()
turtle.goto(-100, 242)
turtle.pendown()

turtle.pensize(10)
turtle.color("black", "red")
turtle.begin_fill()
for x in range(sides):
    turtle.pendown()
    turtle.forward(length)
    turtle.right(angle)
turtle.end_fill()

turtle.penup()
turtle.goto(-175,-75)
turtle.color("white")
turtle.write("STOP",font=("Arial", 100))

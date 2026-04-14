import turtle

def triangle(x1, y1, x2, y2, x3, y3, color):
    turtle.penup()
    turtle.goto(x1, y1)
    turtle.pendown()

    turtle.color(color)
    turtle.begin_fill()

    turtle.goto(x2, y2)
    turtle.goto(x3, y3)
    turtle.goto(x1, y1)

    turtle.end_fill()

def square(x, y, size):
    triangle(x, y, x + size, y, x + size, y + size, "blue")

    triangle(x, y, x, y + size, x + size, y + size, "lightblue")

turtle.speed(0)

size = 40

for i in range(8):
    for j in range(8):
        square(i * size, j * size, size)

turtle.done()
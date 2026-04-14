import turtle

def draw_square(size, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()

def draw_triangle(size, color):
    turtle.color(color)
    turtle.begin_fill()
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()

def draw_circle(radius, color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

turtle.speed(0)

for i in range(5):
    for j in range(5):
        turtle.penup()
        turtle.goto(i * 60, j * 60)
        turtle.pendown()

        if (i + j) % 2 == 0:
            draw_square(40, "blue")
        else:
            draw_triangle(40, "lightblue")

turtle.done()
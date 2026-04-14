import turtle
import random

turtle.speed(0)
turtle.bgcolor("black")

def draw_stars(count):
    turtle.color("white")

    for _ in range(count):
        x = random.randint(-300, 300)
        y = random.randint(0, 300)

        turtle.penup()
        turtle.goto(x, y)
        turtle.dot(2)

def draw_building(x, width, height):
    turtle.penup()
    turtle.goto(x, -200)
    turtle.pendown()

    turtle.color("darkblue")
    turtle.begin_fill()

    for _ in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()

def draw_windows(x, width, height):
    turtle.color("yellow")

    for i in range(x + 5, x + width - 5, 15):
        for j in range(-190, -200 + height - 10, 20):
            if random.choice([True, False]):
                turtle.penup()
                turtle.goto(i, j)
                turtle.dot(5)

def draw_moon():
    turtle.penup()
    turtle.goto(200, 200)
    turtle.pendown()

    turtle.color("lightyellow")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

draw_stars(100)
draw_moon()

x = -300

for _ in range(8):
    w = random.randint(40, 80)
    h = random.randint(100, 250)

    draw_building(x, w, h)
    draw_windows(x, w, h)

    x += w + 10

turtle.done()
from turtle import *

WIDTH = 300
HEIGHT = 200


def rectangle(w: float, h: float):
    """Draws a rectangle of the given width and height."""
    forward(w)
    right(90)
    forward(h)
    right(90)
    forward(w)
    right(90)
    forward(h)
    right(90)


speed(8)
title('Le Tricolore')

penup()
goto(-WIDTH / 2, HEIGHT / 2)
pendown()

pencolor('black')
pensize(2)
rectangle(WIDTH, HEIGHT)
penup()

fillcolor('blue')
begin_fill()
rectangle(WIDTH / 3, HEIGHT)
end_fill()

forward(2 * WIDTH / 3)

fillcolor('red')
begin_fill()
rectangle(WIDTH / 3, HEIGHT)
end_fill()

hideturtle()
done()


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

forward(WIDTH - WIDTH / 3)

fillcolor('red')
begin_fill()
rectangle(WIDTH / 3, HEIGHT)
end_fill()

hideturtle()
done()


def filled_rectangle(width: float, height: float, color: str):
    """Draws a filled rectangle of the given width, height
    and fill color.
    """
    pass

def draw_tricolor(left_color: str, right_color: str):
    """Draws a 300-by-200 vertical (France-style) tricolor
    flag with the given colors. (The center stripe is white.)
    """
    pass

def draw_tricolor(color1: str, color2: str, horiz: bool = False):
    """Draws a 300-by-200 tricolor flag with the given colors.
    If `horiz` is True, the stripes are vertical (like France);
    if `horiz` is False, the stripes are horizontal (like Russia).
    """
    pass




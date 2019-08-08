from turtle import *
from typing import Union


# An optional color is either a color name or `None`.
opt_color = Union[str, None]


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
   
   
def filled_rectangle(w: float, h: float, color: str):
    """Draws a filled rectangle with the given dimensions
    and fill color.
    """
    fillcolor(color)
    begin_fill()
    rectangle(w, h)
    end_fill()
    
    
def jump_by(dx: float = 0, dy: float = 0):
    """Moves the turtle by the given displacements with
    the pen up.
    """
    saved = pen()
    penup()
    setx(xcor() + dx)
    sety(ycor() + dy)
    pen(saved)
 
 
def jump_to(x: float, y: float):
    """Moves the turtle to the given coordinates with the
    pen up.
    """
    saved = pen()
    penup()
    goto(x, y)
    pen(saved)
    
    
def vertical_tricolor(width: float, height: float,
                      color1: str, color2: str, color3: str):
    """Draws a France-style tricolor flag."""
    filled_rectangle(width / 3, height, color1)
    forward(width / 3)
    filled_rectangle(width / 3, height, color2)
    forward(width / 3)
    filled_rectangle(width / 3, height, color3)
    forward(width / 3)


def horizontal_tricolor(width: float, height: float,
                        color1: str, color2: str, color3: str):
    """Draws a Russia-style tricolor flag."""
    filled_rectangle(width, height / 3, color1)
    jump_by(0, -height / 3)
    filled_rectangle(width, height / 3, color2)
    jump_by(0, -height / 3)
    filled_rectangle(width, height / 3, color3)
    jump_by(0, -height / 3)


def horizontal_tricolor_alt(width: float, height: float,
                            color1: str, color2: str, color3: str):
    """Draws a Russia-style tricolor flag."""
    forward(width)
    right(90)
    vertical_tricolor(height, width, color1, color2, color3)
    backward(height)
    left(90)


def tricolor(width: float, height: float,
             color1: str, color2: str, color3: str,
             horizontal: bool = False):
    """Draws a tricolor flag with vertical (France-style) or
    horizontal (Russia-style) stripes.
    """
    if horizontal:
        horizontal_tricolor(width, height, color1, color2, color3)
    else:
        vertical_tricolor(width, height, color1, color2, color3)
        
        
def regular_polygon(size: float, n: int, fill: opt_color = None):
    """Draws a regular polygon with `n` side length `size`,
    optionally filled.
    """
    angle = 360 / n
    if fill is not None:
        fillcolor(fill)
        begin_fill()
    for _ in range(n):
        forward(size)
        right(angle)
    if fill is not None:
        end_fill()
        

def star5(size: float):
    """Draws a five-pointed star."""
    for _ in range(5):
        forward(size)
        left(72)
        forward(size)
        right(144)

        
def star(size: float, n: int = 5, fill: opt_color = None):
    """Draws an `n`-pointed star, possibly filled."""
    outer_angle = 180 - 180 / n
    inner_angle = outer_angle - 360 / n
    old_x, old_y = pos()
    if fill is not None:
        fillcolor(fill)
        begin_fill()
    for _ in range(n):
        forward(size)
        left(inner_angle)
        forward(size)
        right(outer_angle)
    if fill is not None:
        end_fill()
    jump_to(old_x, old_y)

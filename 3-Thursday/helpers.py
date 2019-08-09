from turtle import *
import attr


def jump_to(x: float, y: float):
    """Moves the turtle to the given coordinates with the
    pen up.
    """
    saved = pen()
    penup()
    goto(x, y)
    pen(saved)


def jump_by(dx: float = 0, dy: float = 0):
    """Moves the turtle by the given displacements with
    the pen up.
    """
    jump_to(xcor() + dx, ycor() + dy)
    
    
def jump_rel(ahead: float = 0, leftward: float = 0):
    """Moves the turtle forward by `ahead` and to its left by
    `leftward`, with the pen up.
    """
    saved = pen()
    penup()
    forward(ahead)
    left(90)
    forward(leftward)
    right(90)
    pen(saved)

    

def record(*args, **kwargs):
    if 'auto_attribs' in kwargs:
        return attr.s(*args, **kwargs)
    else:
        return attr.s(*args, auto_attribs=True, **kwargs)


Factory = attr.Factory

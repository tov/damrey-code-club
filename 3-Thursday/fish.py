from math import pi, atan2, sin, sqrt
from turtle import *
from helpers import *


def deg_to_rad(deg: float) -> float:
    """Converts degrees to radians."""
    return pi * deg / 180


def rad_to_deg(deg: float) -> float:
    """Converts degrees to radians."""
    return 180 * deg / pi


def sqr(n: float) -> float:
    """Squares a number."""
    return n * n


@record
class Fish:
    """Represents a fish."""
    name: str
    color: str
    length: float
    body_arc: float = 330
    body_frac: float = 2/3
    tail_frac: float = 1


def draw_fish(f: Fish):
    """Draws a fish."""
    height         = f.body_frac * f.length
    tail_height    = f.tail_frac * height
    body_radius    = height / 2
    body_gap_angle = (360 - f.body_arc) / 2
    body_y0        = body_radius * sin(deg_to_rad(body_gap_angle))
    body_angle0    = 90 - body_gap_angle
    diag_height    = tail_height / 2 - body_y0
    diag_width     = f.length - height
    diag_length    = sqrt(sqr(diag_width) + sqr(diag_height))
    diag_angle     = rad_to_deg(atan2(diag_height, diag_width))
    # Remember where we started and jump to where the tail should start:
    x0, y0 = pos()
    jump_rel(0, (tail_height - height) / 2)
    # Prepare to fill:
    fillcolor(f.color)
    begin_fill()
    # Outline the tail and body:
    right(diag_angle)
    forward(diag_length)
    left(diag_angle + body_angle0)
    circle(-body_radius, f.body_arc)
    left(diag_angle + body_angle0)
    forward(diag_length)
    right(90 + diag_angle)
    forward(tail_height)
    # Fill tail and body:
    end_fill()
    # Return to starting point, then jump to eye position and
    # draw eye:
    jump_to(x0, y0)
    jump_rel(-1/2 * height, -4/5 * f.length)
    fillcolor('white')
    begin_fill()
    circle(height / 15)
    end_fill()
    # Return to starting point and heading:
    jump_to(x0, y0)
    right(90)

    

speed(0)
pensize(2)

nemo = Fish('Nemo', 'blue', 200, body_arc = 270)
salmon = Fish('Salmon', 'gray', 300)

draw_fish(nemo)
right(180)
draw_fish(salmon)

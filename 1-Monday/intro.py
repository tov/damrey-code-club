### Our first Python code

CM_PER_IN = 2.54

def in_to_cm(i: float) -> float:
    """Converts inches to centimeters."""
    return CM_PER_IN * i

assert in_to_cm(1) == 2.54
assert in_to_cm(10) == 25.4

def f_to_c(f: float) -> float:
    """Converts Fahrenheit to Celsius"""
    return (f - 32) / 1.8

assert f_to_c(212) == 100
assert f_to_c(-40) == -40

### How to get access to turtle commands:

# from turtle import *

### Turtle commands we know:

# forward(pixels)
# right(degrees)
# left(degrees)
# pencolor(color)
# fillcolor(color)
# pensize(pixels)
# penup()
# begin_fill()
# end_fill()




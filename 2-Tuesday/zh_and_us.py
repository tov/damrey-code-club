from turtle import *
from flag_helpers import *


def china(width: float):
    """Draws the flag of China."""
    height = 2 * width / 3
    # Remember the location, heading, and pen state:
    old_x, old_y = pos()
    old_h = heading()
    # Do the drawing
    filled_rectangle(width, height, 'red')
    penup()
    jump_by(width / 15, -height / 4)
    star(width / 10, fill = 'yellow')
    jump_by(width / 4, height / 5)
    right(15)
    for _ in range(4):
        right(30)
        star(width / 45, fill = 'yellow')
        forward(width / 10)
    # Restore the saved state:
    jump_to(old_x + width, old_y)
    seth(old_h)
    pendown()


def usa(width: float,
        stripes: int = 13,
        columns: int = 7,
        rows: int = 9):
    """Draws the flag of the United States."""
    old_x, old_y = pos()
    height    = 2 * width / 3
    stripe_ht = height / stripes
    canton_ht = (stripes + 1) // 2 * stripe_ht
    canton_wd = width / 2
    star_dx   = canton_wd / columns
    star_dy   = 0.9 * canton_ht / rows
    star_y0   = old_y - 0.7 * star_dy
    star_size = star_dx / 5
    penup()
    for row in range(stripes):
        if row % 2 == 0:
            filled_rectangle(width, stripe_ht, 'red')
        else:
            filled_rectangle(width, stripe_ht, 'white')
        jump_by(0, -stripe_ht)
    jump_to(old_x, old_y)
    filled_rectangle(canton_wd, canton_ht, 'blue')
    for row in range(rows):
        if row % 2 == 0:
            row_size = columns
            star_x0 = old_x + 0.2 * star_dx
        else:
            row_size = columns - 1
            star_x0 = old_x + 0.7 * star_dx
        for col in range(row_size):
            x = star_x0 + col * star_dx
            y = star_y0 - row * star_dy
            jump_to(x, y)
            star(star_size, fill = 'yellow')
    pendown()
    jump_to(old_x, old_y)
    rectangle(width, height)


speed(0)

jump_to(-290, 210)
china(300)

jump_to(-10, -10)
usa(300)

exitonclick()
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
    
    
def is_even(z: int) -> bool:
    """Determines whether an integer is even."""
    return z % 2 == 0


def usa(width: float,
        stripes: int = 13,
        columns: int = 7,
        rows: int = 9):
    """Draws the flag of the United States."""
    old_x, old_y = pos()
    # Calculate various dimensions:
    height    = 2 * width / 3
    stripe_ht = height / stripes                # stripe thickness
    canton_ht = (stripes + 1) // 2 * stripe_ht  # height of blue canton
    canton_wd = width / 2                       # width of blue canton
    star_dx   = canton_wd / columns             # horiz. displacement of stars
    star_dy   = 0.9 * canton_ht / rows          # vert. displacement of stars
    star_y0   = old_y - 0.7 * star_dy           # y coordinate of top star row
    star_size = star_dx / 5                     # size of each star
    margin_x  = star_dx / 5                     # star field left margin size
    # Draw the stripes:
    penup()
    for row in range(stripes):
        if is_even(row):
            filled_rectangle(width, stripe_ht, 'red')
        else:
            filled_rectangle(width, stripe_ht, 'white')
        jump_by(0, -stripe_ht)
    # Draw the blue canton:
    jump_to(old_x, old_y)
    filled_rectangle(canton_wd, canton_ht, 'blue')
    # Draw the stars:
    for row in range(rows):
        if is_even(row):
            row_size = columns
            star_x0 = old_x + margin_x
        else:
            row_size = columns - 1
            star_x0 = old_x + margin_x + star_dx / 2
        for col in range(row_size):
            x = star_x0 + col * star_dx
            y = star_y0 - row * star_dy
            jump_to(x, y)
            star(star_size, fill = 'white')
    # Outline the whole thing:
    pendown()
    jump_to(old_x, old_y)
    rectangle(width, height)


speed(0)

jump_to(-290, 210)
china(300)

jump_to(-10, -10)
usa(300)

exitonclick()

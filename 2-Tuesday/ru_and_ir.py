from turtle import *
from flag_helpers import *


def russia(width: float):
    """Draws the flag of the Russian Federation."""
    tricolor(width, 2 * width / 3, 'white', 'blue', 'red', True)
  
  
def ireland(width: float):
    """Draws the flag of the Irish Republic."""
    tricolor(width, width / 2, 'green', 'white', 'orange')
 

speed(0)
        
jump_to(-290, 250)
russia(300)

jump_to(-10, -40)
ireland(300)

done()
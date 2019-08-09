from math import inf
from turtle import *
from typing import Optional
from helpers import *

# Aquarium dimensions
WIDTH = 1000
HEIGHT = 1000


@record
class Fish:
    size: float
    color: str
  

FISH1 = Fish(50, 'blue')
FISH2 = Fish(75, 'orange')
  

@record
class Posn:
    x: float
    y: float


@record
class PositionedFish:
    fish: Fish
    posn: Posn


@record
class OneMoreFish:
    first: PositionedFish
    rest:  Optional['OneMoreFish']


Aquarium = Optional[OneMoreFish]


AQ1 = OneMoreFish(
          PositionedFish(Fish(100, 'black'), Posn(100, -200)),
          OneMoreFish(
              PositionedFish(FISH2, Posn(60, 90)),
              OneMoreFish(
                  PositionedFish(FISH1, Posn(0, 0)),
                  OneMoreFish(
                      PositionedFish(Fish(20, 'silver'), Posn(-200, -300)),
                      None))))


def render_single_fish(f: Fish, p: Posn):
    """Renders fish `f` at position `p`."""
    penup()
    goto(p.x, p.y)
    pendown()
    fillcolor(f.color)
    begin_fill()
    circle(f.size)
    end_fill()  


def render_aquarium(aq: Aquarium):
    """Renders the fish in the aquarium."""
    penup()
    goto(-WIDTH/2, HEIGHT/2)
    fillcolor('darkblue')
    begin_fill()
    for _ in range(2):
        forward(WIDTH)
        right(90)
        forward(HEIGHT)
        right(90)
    end_fill()
    render_fish_list(aq)


@record
class Node:
    first: int
    rest: Optional['Node']
    
    
LinkedList = Optional[Node]


EX_LIST0 = None
EX_LIST1 = Node(2, Node(3, Node(7, Node(19, None))))
EX_LIST2 = Node(-6, EX_LIST1)


def fold_right(plus, zero, lst: LinkedList) -> int:
    if lst is None:
        return zero
    else:
        return plus(lst.first, fold_right(plus, zero, lst.rest))


def sum_list(lst: LinkedList) -> int:
    """Sums the integers in a linked list."""
    return fold_right(lambda x, y: x + y, 0, lst)


def max_list(lst: LinkedList) -> int:
    """Returns the largest element in a linked list, or -inf if
    empty.
    """
    return fold_right(max, -inf, lst)
  

assert max_list(None) == -inf
assert max_list(Node(2, Node(5, None))) == 5
assert max_list(Node(5, Node(2, None))) == 5
assert max_list(Node(5, Node(20, Node(6, None)))) == 20


def iota(n: int) -> LinkedList:
    lst = None
    for i in range(n):
        lst = Node(n - i, lst)
    return lst


### EXERCISE 1

# Complete these functions `fold_right` and write at least three tests for each:

def prod_list(lst: LinkedList) -> int:
    """Multiplies the integers in a linked list."""
    pass


def count_occurrences(needle: int, haystack: LinkedList) -> int:
    """Counts the number of tines that `needle` occurs in
    `haystack`.
    """
    pass


### EXERCISE 2

# Complete this function using either/both recursion or `fold_right`.

def comma_separate(lst: LinkedList) -> str:
    """Returns a string containing the integers in `lst`, separated
    by commas.
    """
    pass

assert comma_separate(None) == ''
assert comma_separate(Node(3, None)) == '3'
assert comma_separate(Node(3, Node(5, Node(7, None)))) == '3, 5, 7'


### EXERCISE 3

# Complete this function using recursion.

def render_fish_list(fishes: Optional[OneMoreFish]):
    """Renders each positioned fish in `fishes`.

    (This means it should call `render_single_fish` on each fish along
    with that fish's position.)
    """
    # ... render_single_fish(apf.fish, apf.posn) ...
    pass


### EXERCISE 4

# Complete this function using `fold_right` or recursion.

def double_list(lst: LinkedList) -> LinkedList:
    pass


assert double_list(None) == None
assert double_list(Node(2, None)) == Node(4, None)
assert double_list(Node(2, Node( 5, Node( 9, None)))) \
                == Node(4, Node(10, Node(18, None)))

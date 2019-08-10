from time import sleep
from turtle import *
from typing import Optional
from helpers import *


@record
class Fish:
    """Represents a fish."""
    size: float
    color: str


# Some example fish:
EX_FISH1 = Fish(50, 'blue')
EX_FISH2 = Fish(75, 'orange')


def draw_fish(f: Fish):
    """Draws fish `f` at the current turtle position."""
    x0, y0 = pos()
    h0 = heading()
    fillcolor(f.color)
    begin_fill()
    left(30)
    for _ in range(3):
        left(120)
        forward(0.4 * f.size)
    right(120)
    circle(0.5 * f.size)
    end_fill()
    jump_rel(0, 0.75 * f.size)
    fillcolor('white')
    begin_fill()
    circle(0.1 * f.size)
    end_fill()
    jump_to(x0, y0)
    setheading(h0)


def feed_fish(f: Fish):
    """Feeds the fish so it grows."""
    f.size *= 1.1


@record
class Posn:
    """Represents the 2-D point (x, y)."""
    x: float
    y: float


@record
class SwimmingFish:
    """Associates a fish with its position and x velocity."""
    fish: Fish
    posn: Posn
    dx:   float


# Some examples of swimming fish:
EX_SWIMMING1 = SwimmingFish(EX_FISH1, Posn(200, -100), -10)
EX_SWIMMING2 = SwimmingFish(EX_FISH2, Posn(-200, 100), 5)


def draw_swimming_fish(f: SwimmingFish):
    """Draws fish `f` at position `p`."""
    jump_to(f.posn.x, f.posn.y)
    if f.dx < 0:
        seth(180)
    else:
        seth(0)
    draw_fish(f.fish)


def left_edge(f: SwimmingFish) -> float:
    """Returns the x coordinate of the left edge of a swimming fish."""
    if f.dx > 0:
        return f.posn.x
    else:
        return f.posn.x - f.fish.size


def right_edge(f: SwimmingFish) -> float:
    """Returns the x coordinate of the right edge of a swimming fish."""
    if f.dx > 0:
        return f.posn.x + f.fish.size
    else:
        return f.posn.x


def move_swimming_fish(f: SwimmingFish, width: int):
    """Moves the fish to simulate swimming."""
    f.posn.x += f.dx
    if (right_edge(f) > width / 2 and f.dx > 0) or \
       (left_edge(f) < -width / 2 and f.dx < 0):
        f.dx = -f.dx


def is_posn_above_fish(p: Posn, f: SwimmingFish):
    """Determines whether `p` is directly above `f`."""
    return p.y > f.posn.y and left_edge(f) <= p.x <= right_edge(f)


def try_feed_fish(p: Posn, f: SwimmingFish):
    """Feeds the fish if `p` is above it."""
    if is_posn_above_fish(p, f):
        feed_fish(f.fish)


FishList = Optional['Node']


@record
class Node:
    """One node in a linked list of `SwimmingFish`s."""
    first: SwimmingFish
    rest:  FishList


# Some examples of lists of fish:
EX_FISHES0 = None
EX_FISHES1 = Node(EX_SWIMMING1, Node(EX_SWIMMING2, None))
EX_FISHES2 = Node(
    SwimmingFish(Fish(60, 'orange'), Posn(60, 90), 10),
    Node(
        SwimmingFish(Fish(75, 'blue'), Posn(0, 0), -10),
        Node(
            SwimmingFish(Fish(20, 'silver'), Posn(-200, -300), 30),
            None)))


def draw_fish_list(fishes: FishList):
    """Renders all the fish in the list."""
    if fishes is not None:
        draw_swimming_fish(fishes.first)
        draw_fish_list(fishes.rest)


def move_fish_list(fishes: FishList, width: int):
    """Moves all the fish in the list to simulate swimming."""
    if fishes is not None:
        move_swimming_fish(fishes.first, width)
        move_fish_list(fishes.rest, width)


def try_feed_all_fish(p: Posn, fishes: FishList):
    """Feeds every fish that `p` is above."""
    if fishes is not None:
        try_feed_fish(p, fishes.first)
        try_feed_all_fish(p, fishes.rest)


@record
class Aquarium:
    """An aquarium full of fish."""
    width:  int
    height: int
    fishes: FishList


# Some examples of aquariums:
EX_AQ1 = Aquarium(640, 480, EX_FISHES1)
EX_AQ2 = Aquarium(800, 800, EX_FISHES2)


def draw_aquarium(aq: Aquarium):
    """Draws the fish in the aquarium."""
    penup()
    goto(-aq.width/2, aq.height/2)
    seth(0)
    fillcolor('darkblue')
    begin_fill()
    for _ in range(2):
        forward(aq.width)
        right(90)
        forward(aq.height)
        right(90)
    end_fill()
    draw_fish_list(aq.fishes)


def move_aquarium(aq: Aquarium):
    """Moves all the fish in the aquarium."""
    move_fish_list(aq.fishes, aq.width)


def animate(aq: Aquarium):
    """Animates the given aquarium."""
    def handle_click(x: float, y: float):
        try_feed_all_fish(Posn(x, y), aq.fishes)

    def handle_tick():
        move_aquarium(aq)
        draw_aquarium(aq)
        update()
        ontimer(handle_tick, 10)

    sc = Screen()
    sc.setup(aq.width, aq.height)
    sc.tracer(0)
    sc.onclick(handle_click)
    hideturtle()
    handle_tick()
    mainloop()


animate(EX_AQ1)

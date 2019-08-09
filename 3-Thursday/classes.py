from math import sqrt
from turtle import *
from typing import Optional

from helpers import *


@record
class Posn:
    """A position on the 2-D plane."""
    x: float
    y: float
    

def manhattan_distance(p1: Posn, p2: Posn) -> float:
    """Computes the Manhattan distance between two positions."""
    dx = abs(p1.x - p2.x)
    dy = abs(p1.y - p2.y)
    return dx + dy


assert manhattan_distance(Posn(0, 0), Posn(7, 9)) == 16
assert manhattan_distance(Posn(3, -6), Posn(1, 6)) == 14


def distance(p1: Posn, p2: Posn) -> float:
    """Computes the distance between two positions."""
    dx = p1.x - p2.x
    dy = p1.y - p2.y
    return sqrt(dx * dx + dy * dy)


assert distance(Posn(0, 0), Posn(3, 4)) == 5
assert distance(Posn(0, 2), Posn(3, -2)) == 5
assert distance(Posn(5, 6), Posn(0, 18)) == 13


@record
class SatScore:
    """Represents a score on the SAT."""
    math: int
    verbal: int
    essay: Optional[int] = None


def is_valid_score(sat: SatScore) -> bool:
    """Returns whether the given score is within the valid
    range. (This means 200–800 for math and verbal, and 20–80
    for essay.)
    """
    return (sat.essay is None or 20 <= sat.essay <= 80) \
       and 200 <= sat.math <= 800 \
       and 200 <= sat.verbal <= 800
       

assert is_valid_score(SatScore(750, 570, 26))
assert is_valid_score(SatScore(750, 570))
assert not is_valid_score(SatScore(750, 1570))
assert not is_valid_score(SatScore(0, 570))
assert not is_valid_score(SatScore(750, 570, 800))


def combined_score(sat: SatScore) -> int:
    """Returns the sum of the math and verbal scores."""
    return sat.math + sat.verbal


assert combined_score(SatScore(600, 550)) == 1150
assert combined_score(SatScore(600, 800, 50)) == 1400


def is_perfect_score(sat: SatScore) -> bool:
    """Returns whether `sat` is a perfect score."""
    return combined_score(sat) == 1600


assert is_perfect_score(SatScore(800, 800))
assert not is_perfect_score(SatScore(800, 790))


def is_no_lower_than(sat1: SatScore, sat2: SatScore) -> bool:
    """Returns whether every part of `sat1` is at least as good
    as every part of `sat2`.
    """
    if sat1.math < sat2.math: return False
    if sat1.verbal < sat2.verbal: return False
    if sat1.essay is None and sat2.essay is None:
        return True
    elif sat1.essay is None and set2.essay is not None:
        return False
    elif sat1.essay is not None and set2.essay is None:
        return True
    else:
        return sat1.essay >= sat2.essay


@record
class MobilePhone:
    brand: str
    model: str
    color: str
    grams: float
    GB: int

# a_phone = MobilePhone('Apple', 'iPhone 3', 'white', 200, 4)
# another_phone = MobilePhone('Samsung', 'Galaxy 13', 'black', 800, 2048)


# EXERCISE 1: An SAT multiple choice question consists of a prompt, three
# answers, and an indication of which answer is correct.
#
#  a) Define a class for an SAT multiple choice question.
#  b) Define a function that prints out an SAT multiple choice question (but
#     doesn't say what the correct answer is).
#  c) Define a function that takes an SAT multiple choice question and a
#     choice (A, B, or C), and returns whether the choice is correct.


# EXERCISE 2: Here is a class defining a fish:

@record
class Fish:
    """Represents a fish."""
    name: str
    color: str
    length: float

# Define a function that takes a `Fish` and draws the fish using turtle
# graphics. The simplest possible fish is a circle of the fish's color
# whose radius is half the length of the fish, and containing a small
# white circle within to represent an eye.


# EXERCISE 3: Think of three kinds of things that you can represent as
# a class. Each should have at least two fields. Write each class, and
# write at least one function that does something for each class.


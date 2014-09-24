from fractions import Fraction
from collections import namedtuple

class Meters(object):
    whole = 1
    dot_half = Fraction(3,4)
    half = Fraction(1, 2)
    dot_quarter = Fraction(3, 8)
    quarter = Fraction(1, 4)
    dot_eighth = Fraction(3, 16)
    eighth = Fraction(1, 8)
    dot_sixteenth = Fraction(3, 32)
    sixteenth = Fraction(1, 16)
    dot_thirtysecond = Fraction(3, 64)
    thirtysecond = Fraction(1, 32)

tab = {"meter": (4,4),
       "partial": 0,
       "strings": ("e,", "a,", "d", "g", "b", "e'"),
       "title": "An Example",
       "composer": "Jason R. Fruit",
       "content":
       [(Meters.quarter, [("0", 0),
                          ("1", 1),
                          ("0", 2),
                          ("3", 4)]),
        (Meters.quarter, [("0", 0),
                          ("1", 1),
                          ("0", 2),
                          ("3", 4)]),
        (Meters.half, [("0", 1),
                       ("1", 1),
                       ("0", 2),
                       ("3", 4)]),
        (Meters.quarter, [("0", 0),
                          ("1", 1),
                          ("0", 2),
                          ("3", 4)]),
        (Meters.quarter, [("0", 0),
                          ("1", 1),
                          ("0", 2),
                          ("3", 4)]),
        (Meters.half, [("0", 1),
                       ("1", 1),
                       ("0", 2),
                       ("3", 4)])]}

class LayoutEngine(object):
    def __init__(self, tab):
        self.tab = tab

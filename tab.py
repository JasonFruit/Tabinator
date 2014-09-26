from fractions import Fraction
from collections import namedtuple
import math

class Durations(object):
    whole = Fraction(1, 1)
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
    dot_sixtyfourth = Fraction(3, 128)
    sixtyfourth = Fraction(1, 64)

meter = namedtuple("meter", "numerator denominator duration")

meters = {"6/4": meter(6, 4, Durations.whole + Durations.half),
          "4/4": meter(4, 4, Durations.whole),
          "3/4": meter(3, 4, Durations.dot_half),
          "2/4": meter(2, 4, Durations.half),
          "12/8": meter(12, 8, Durations.dot_quarter * 4),
          "9/8": meter(9, 8, Durations.dot_half + Durations.dot_quarter),
          "6/8": meter(6, 8, Durations.dot_half),
          "3/8": meter(3, 8, Durations.dot_quarter),
          "2/8": meter(2, 8, Durations.quarter)}

class TabDrawer(object):
    def __init__(self, tab, top=20, spacing=18):

        self.tab = tab
        self.string_count = len(self.tab["strings"])
        self.top = top
        self.spacing = spacing

        self.measure_duration = meters[tab["meter"]].duration
        self.min_space = 20

        # start with an irrationally large minimum duration
        self.min_duration = Durations.whole

        # find the shortest duration in the tab
        for duration in [note[0] 
                         for note in self.tab["content"]]:
            if duration < self.min_duration:
                self.min_duration = duration
                
    def _note_space(self, duration):
        return (self.min_space * 
                (math.log(duration / self.min_duration, 2) + 1))

    def draw(self, canvas):
        x = 20
        canvas.draw_strings(self.top, self.spacing, self.string_count)
        canvas.draw_strings(self.top + self.spacing * 10, 
                            self.spacing, 
                            self.string_count)
        for note in self.tab["content"]:
            for glyph in note[1]:
                symbol, string = glyph
                canvas.draw_note(symbol, string, x, self.top, self.spacing)
            x += self._note_space(note[0])

if __name__ == "__main__":

    tab = {"meter": "4/4",
           "partial": 0,
           "strings": ("e,", "a,", "d", "g", "b", "e'"),
           "title": "An Example",
           "composer": "Jason R. Fruit",
           "content":
           [(Durations.quarter, [("0", 0),
                                 ("1", 1),
                                 ("0", 2),
                                 ("3", 4)]),
            (Durations.quarter, [("0", 0),
                                 ("1", 1),
                                 ("0", 2),
                                 ("3", 4)]),
            (Durations.half, [("0", 1),
                              ("1", 1),
                              ("0", 2),
                              ("3", 4)]),
            (Durations.quarter, [("0", 0),
                                 ("1", 1),
                                 ("0", 2),
                                 ("3", 4)]),
            (Durations.quarter, [("0", 0),
                                 ("1", 1),
                                 ("0", 2),
                                 ("3", 4)]),
            (Durations.half, [("0", 1),
                              ("1", 1),
                              ("0", 2),
                              ("3", 4)])]}
    
    td = TabDrawer(tab)
    td.draw(None)

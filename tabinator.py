import Tkinter as tk
import os
from tab import *

tablature = {"meter": "4/4",
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
              (Durations.half, [("1", 0),
                                ("1", 1),
                                ("2", 2),
                                ("3", 3)]),
              (Durations.quarter, [("0", 0),
                                   ("1", 1),
                                   ("0", 2),
                                   ("3", 4)]),
              (Durations.quarter, [("0", 0),
                                   ("1", 1),
                                   ("0", 2),
                                   ("3", 4)]),
              (Durations.half, [("1", 0),
                                ("1", 1),
                                ("2", 2),
                                ("3", 3)])]}

class TabCanvas(tk.Canvas):
    def __init__(self, parent, **kwargs):
        apply(tk.Canvas.__init__, [self, parent], kwargs)
    def _string_y(self, string, top, spacing):
        return top + string * spacing
    def draw_strings(self, top=20, spacing=18, strings=6):
        for string in range(strings):
            y = self._string_y(string, top, spacing)
            self.create_line(0, y, self.winfo_screenwidth(), y)
    def draw_note(self, symbol, string, x_value, top=20, spacing=18):
        x = x_value
        y = self._string_y(string, top, spacing)
        self.create_text((x, y),
                         text=symbol,
                         font=("Times New Roman", 12))
                         
            

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.drawer = TabDrawer(tablature)
        self.title("The Tabinator")
        self.line_start = None
        self.canvas = TabCanvas(self, width=300, height=300, bg="white")

        self.button = tk.Button(self, text="Generate PDF",
                                command=self.generate_pdf)
        self.button2 = tk.Button(self, text="Add Text",
                                 command=self.draw_tab)
        self.canvas.pack()
        self.button.pack(pady=10)
        self.button2.pack(pady=10)

    def draw_tab(self):
        self.drawer.draw(self.canvas)

    def generate_pdf(self):
        self.canvas.postscript(file="tmp.ps", colormode='color')
        os.system("ps2pdf tmp.ps result.pdf")
        os.remove("tmp.ps")
        self.destroy()

app = App()
app.mainloop()

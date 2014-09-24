import Tkinter as tk
import os

class TabCanvas(tk.Canvas):
    def __init__(self, parent, **kwargs):
        apply(tk.Canvas.__init__, [self, parent], kwargs)
    def _string_y(self, string):
        return 20 + string * 18
    def draw_strings(self, strings=6):
        for string in range(strings):
            y = self._string_y(string)
            self.create_line(0, y, self.winfo_screenwidth(), y)
    def draw_note(self, symbol, string, x_value):
        x = x_value
        y = self._string_y(string)
        self.create_text((x, y),
                         text=symbol,
                         font=("Times New Roman", 12))
                         
            

class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("The Tabinator")
        self.line_start = None
        self.canvas = TabCanvas(self, width=300, height=300, bg="white")
        self.canvas.draw_strings()
        
        self.canvas.draw_note("0", 0, 20)
        self.canvas.draw_note("1", 1, 20)
        self.canvas.draw_note("0", 2, 20)
        self.canvas.draw_note("3", 4, 20)

        self.canvas.draw_note("0", 0, 45)
        self.canvas.draw_note("1", 1, 45)
        self.canvas.draw_note("0", 2, 45)
        self.canvas.draw_note("3", 4, 45)

        self.canvas.draw_note("1", 0, 70)
        self.canvas.draw_note("1", 1, 70)
        self.canvas.draw_note("2", 2, 70)
        self.canvas.draw_note("3", 3, 70)
        
        self.canvas.bind("<Button-1>", lambda e: self.draw(e.x, e.y))
        self.button = tk.Button(self, text="Generate PDF",
                                command=self.generate_pdf)
        self.button2 = tk.Button(self, text="Add Text",
                                 command=self.add_text)
        self.canvas.pack()
        self.button.pack(pady=10)
        self.button2.pack(pady=10)

    def draw(self, x, y):
        if self.line_start:
            x_origin, y_origin = self.line_start
            self.canvas.create_line(x_origin, y_origin, x, y)
            self.line_start = None
        else:
            self.line_start = (x, y)

    def add_text(self):
        self.canvas.create_text(self.line_start,
                                text="Text",
                                font=("Helvetica", "24"),
                                fill="red")
        self.line_start = None

    def generate_pdf(self):
        self.canvas.postscript(file="tmp.ps", colormode='color')
        os.system("ps2pdf tmp.ps result.pdf")
        os.remove("tmp.ps")
        self.destroy()

app = App()
app.mainloop()

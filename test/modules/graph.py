from Tkinter import *


class Graph(object):
    def __init__(self, obj):
        self.canvas = obj

    def draw_graph(self, y):
        self.clean_canvas()

        #  X axis advance
        delta_x = self.canvas.winfo_width() / float(len(y))
        t = 0.0

        # Y axis calculation helpers
        rango = abs(min(y) - max(y))
        canvas_h = self.canvas.winfo_height()
        delta_y = canvas_h / float(rango)
        min_y = min(y)

        prev_y = 0

        for index, i in enumerate(y):

            if index == 0:
                y1 = 0
            else:
                y1 = prev_y

            x1 = t

            t += delta_x
            y2 = canvas_h - ((i - min_y) * delta_y)

            self.draw_line(x1, y1, t, y2)

            prev_y = y2

        print "Plot finished"

    def draw_line(self, x1, y1, x2, y2):
        self.canvas.create_line(x1, y1, x2, y2, fill="#94004A")

    def clean_canvas(self):
        print 'Graph Clean'
        self.canvas.delete(ALL)

    def __del__(self):
        print 'Graph died'

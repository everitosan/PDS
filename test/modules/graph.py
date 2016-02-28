from Tkinter import *


class Graph(object):
    def __init__(self, obj):
        self.canvas = obj
        self.line = self.canvas.create_line([0, 0, 50, 50, 100, 50, 800, 400], fill="#94004A")
        self.data = []

    def draw_graph(self, y):

        #  X axis advance
        delta_x = self.canvas.winfo_width() / float(len(y))
        t = 0.0

        # Y axis calculation helpers
        rango = abs(min(y) - max(y))
        canvas_h = self.canvas.winfo_height()
        delta_y = canvas_h / float(rango)
        min_y = min(y)

        for index, i in enumerate(y):

            y2 = canvas_h - ((i - min_y) * delta_y)

            self.data.append(t)
            self.data.append(y2)

            t += delta_x

        print "%d -> %d * 2" % (len(self.data), len(y))

        self.draw_line()

    def draw_line(self):
        # self.clean_canvas()
        # self.canvas.coords(self.line, 0, 0, 500, 100, 1200, 400)
        self.line = self.canvas.create_line(self.data, fill="#94004A")
        self.canvas.itemconfig(self.line, fill="green")
        print "Plot finished"

    def clean_canvas(self):
        print 'Graph Clean'
        self.canvas.delete(ALL)

    def __del__(self):
        print 'Graph died'

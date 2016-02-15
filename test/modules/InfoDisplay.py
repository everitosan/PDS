from Tkinter import *
from tkFont import *


class InfoDisplay(object):
    def __init__(self, container, n_row, n_column, text, variable_text):

        # bold_font = Font(family="Lantinghei SC", size=14, weight="bold", underline=1)
        normal_font = Font(family="Lantinghei SC", size=12, weight="normal", underline=0)

        static_label = Label(container, text=text, font=normal_font)
        static_label.grid(row=n_row, column=n_column)

        variable_label = Label(container, textvariable=variable_text, font=normal_font)
        variable_label.grid(row=n_row+1, column=n_column)

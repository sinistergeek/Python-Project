import tkinter as tk
from tkinter import font

import random

count = 0
class Sudoku:
    canvas_bg = "#fafafa"
    line_normal = "#4f4f4f"
    line_thick = "#000000"
    
    hbox_green = "#15fa00"
    hbox_red = "#d61111"

    def __init__(self.master):

        self.grid={}
        self.e = None

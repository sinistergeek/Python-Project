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

        self.canvas_width = 300
        self.canvas_height = 300
        self.canvas = tk.Canvas(master,bg=self.vanvas_bg,width=self.canvas_width,height=self.vanvas_height)
        self.t = tk.Entry(self.canvas)
        self.t.bind("<KeyRelease>",self.keyPressed)
        self.canvas.grid(columnspan=3)
        self.canvas.bind("<Button 1>",self.click)
        self.btn_solve = tk.Button(master,text='Solve',command=self.warpper,width=8)
        self.btn_solve.grid(row=1,padx=5,pady=5)
        self.btn_gen = tk.Button(master,text='Generate',command=self.Generate,width=8)
        self.btn_gen.grid(row=1,column=1,padx=5,pady=5,sticky=tk.E)
        self.set_difficulty = tk.IntVar(master,1)
        self.difficulty_selector = tk.OptionMenu(master,self.set_difficulty,1,2,3,4,5)
        self.difficulty_selector.grid(row=1,column=2,pady=5,sticky=tk.W)
        self.cell_width = self.canvas_width/9
        self.cell_height = self.canvas_height/9
        for x in range(1,9):
            width = 1
            fill = self.line_normal
            if(x%3==0):
                width=2
                fill = self.line_thick
            else:
                width=1
                fill = self.line_normal
            self.canvas.create_line(self.cell_width*x,0,self.cell_width*x,self.canvas_height,width=width,fill=fill)
        for y in range(1,9):
            width=1
            fill = self.line_normal
            if(y%3==0):
                width=2
                fill=self.line_thick
            else:
                width=1
                fill=self.line_normal
            self.canvas.create_line(0,self.cell_height*y,self.canvas_width,self.cell_height*y,width=width,fill=fill)
    def click(self,eventorigin):
        x= eventorigin.x
        y= eventorigin.y
        rect_x = int(x/self.cell_width)*self.cell_width
        rect_y = int(y/self.cell_height)*self.cell_height
        coords=[rect_x,rect_y,rect_x+self.cell_width,rect_y,rect_x+self.cell_width,rect_y+cell_height.rect_x,rect_y+self.cell_height]
        editable = self.getCell(x/self.cell_width,y/self.cell_height)[1]
        if editable:
            h_box = self.canvas.create_polygon(coords,outline=self.hbox_green,fill='',width=3)
            self.edit(rect_x,rect_y)
        else:
            h_box = self.canvas.create_polygon(coords,outline=self.hbox_red,fill='',width=3)
        self.canvas.after(200,lambda:self.canvas.delete(h_box))

    def edit(self,cordx:int,cordy:int):
        if self.e is None:
            pass
        else:
            self.canvas.delete(self.e)
        self.e = self.canvas.create_window(cordx+1,cordy+1,window=self.t,width=self.cell_width-1,height=self.cell_height-2,anchor=tk.NW)


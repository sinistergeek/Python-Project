from tkinter import *
import tkinter.font

class PaintApp:
    drawing_tool = "pencil"
    left_button = "up"

    x_position,y_position = None,None
    x1_line_pt,y1_line_pt,x2_line_pt,y2_line_pt = None,None,None,None

    @staticmethod
    def quit_app(event=None):
        root.quit()

    def __init__(self,root):
        drawing_area = Canvas(root)
        drawing_area.pack()

        drawing_area.bind("<Motion>",self.motion)
        drawing_area.bind("<ButtonPress-1>",self.left_button_down)
        drawing_area.bind("<ButtonRelease-1>",self.left_button_up)
        the_menu = Menu(root)

        file_menu = Menu(the_menu,tearoff=0)
        file_menu.add_command(label="Line",command=self.set_line_drawing_tool)
        file_menu.add_command(label="Pencil",command=self.set_pencil_drawing_tool)
        file_menu.add_command(label="ARC",command=self.set_arc_drawing_tool)
        file_menu.add_command(label="Rectangle",command=self.set_rectangle_drawing_tool)
        file_menu.add_command(label="Oval",command=self.set_oval_drawing_pool)
        file_menu.add_command(label="Text",command=self.set_text_drawing_tool)


        file_menu.add_separator()
        file_menu.add_command(label="Quit",command=self.quit_app)
        the_menu.add_cascade(label="Options",menu=file_menu)
        root.config(menu=the_menu)

        def set_line_drawing_tool(self):
            self.drawing_tool = "line"

        def set_pencil_drawing_tool(self):
            self.drawing_tool = "pencil"
        def set_arc_drawing_tool(self):
            self.drawing_tool = "arc"

        def set_rectangle_drawing_tool(self):
            self.drawing_tool = "rectange"

        def set_oval_drawing_tool(self):
            self.drawing_tool = "oval"

        def left_button_down(self,event=None):
            self.left_button= "down"
            self.x1_line_pt = event.x
            self.y1_line_pt = event.y

        def left_button_up(self,event=None):
            self.left_button = "up"
            self.x_position = None
            self.y_position = None
            self.x2_line_pt = event.x
            self.y2_line_pt = event.y

            if self.drawing_tool == "line":
                self.line_draw(event)
            if self.drawing_tool == "pencil":
                self.pencil_draw(event)
            if self.drawing_tool == "arc":
                self.arc_draw(event)
            if self.drawing_tool == "oval":
                self.oval_draw(event)
            if self.drawing_tool == "rectangle":
                self.rect_draw(event)
            if self.drawing_tool == "text":
                self.text_draw(event)


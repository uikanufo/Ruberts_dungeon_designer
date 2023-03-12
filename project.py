from tkinter import *
from tkinter import ttk, simpledialog
from math import floor 
import pickle

class Project:


    def draw_black_line(self, x0, y0, x1, y1):
        return self.C.create_line(x0, y0, x1, y1, fill="black", tags = "line")

    def grid_function(self, size:int, window_width, window_height):

        global vert_line_coordinates
        global hori_line_coordinates 
        hori_line = 0
        vert_line = 0
        while vert_line != floor(window_width/size):
            self.draw_black_line(0, vert_line*size, window_width, (vert_line*size)) #Horizontal lines
            #Appends tuples with the coordinates of the particular line into the list
            self.hori_line_coordinates.append(((0, vert_line*size), (window_width, vert_line*size),))
            vert_line += 1
        while hori_line != floor(window_height/size):
            self.draw_black_line((hori_line*size), 0, (hori_line*size), window_height) #Vertical lines
            self.vert_line_coordinates.append(((hori_line*size, 0), (window_height, hori_line*size),))
            hori_line += 1

    def save_project(self):
        """Useless for now"""
        this_project = pickle.dumps(self)
        return this_project

    def load_project(self, root, window_height, window_width):
        self.C = Canvas(root, bg="white",
                height=window_height, width=window_width)
        

        self.grid_function(20, window_width, window_height)
        

        self.C.pack()

    def draw_square(self, mouse_coordinates):
        self.C.create_rectangle(mouse_coordinates[0],
        mouse_coordinates[1], 
        mouse_coordinates[0],
        mouse_coordinates[1])



    def __init__(self, root, window_height, window_width) -> None:
        #These lists store the start and end points of lines as tuples of two tuples
        self.vert_line_coordinates = []
        self.hori_line_coordinates = []
        self.name = simpledialog.askstring("", "Name the project")
        #for vali in range(C.cget(height)/10):
        self.load_project(root, window_height, window_width)

            


    def unload_canvas(self):
        self.C.destroy()
    

    

from tkinter import *
from tkinter import ttk, simpledialog
from math import floor 
import pickle

class Project:

    

    def draw_grey_line(self, x0, y0, x1, y1):
        return self.C.create_line(x0, y0, x1, y1, fill="grey", tags = "line")

    def grid_function(self, size:int, window_width, window_height):
        """Draws a grey grid. Keep in mind the offset of +1 for the startpoint of lines"""

        global vert_line_coordinates
        global hori_line_coordinates 
        hori_line = 0
        vert_line = 0

        while vert_line != floor(window_width/size)+1:
            self.draw_grey_line(0, (vert_line*size)+1, window_width, (vert_line*size)+1) #Horizontal lines
            #Appends tuples with the coordinates of the particular line into the list
            self.hori_line_coordinates.append(((0, vert_line*size), (window_width, vert_line*size),))
            vert_line += 1

        while hori_line != floor(window_height/size)+1:
            self.draw_grey_line((hori_line*size)+1, 0, (hori_line*size)+1, window_height) #Vertical lines
            self.vert_line_coordinates.append(((hori_line*size, 0), (window_height, hori_line*size),))
            hori_line += 1

    def save_project(self):
        saved_project = Saved_project(self)
        return pickle.dumps(saved_project)

    def load_canvas(self, root, window_height, window_width):
        self.C = Canvas(root, bg="white",
                height=window_height, width=window_width)
        

        self.grid_function(self.size, window_width+1, window_height+1)
        

        self.C.pack()


    def draw_black_line(self, coordinates:tuple):
        self.C.create_line(coordinates[0], coordinates[1], 
                           coordinates[2], coordinates[3]) #Meant to correspond to (x0, y0), (x1, y1)
        self.lines.append(coordinates)

    def draw_square(self, mouse_coordinates):
        lining = self.draw_black_line 
        x0 = mouse_coordinates[0]
        y0 = mouse_coordinates[1]
        offset = self.size

            
        lining((x0, y0, x0+offset, y0)) 
        lining((x0, y0, x0, y0+offset)) 
        lining((x0+offset, y0+offset, x0, y0+offset)) 
        lining((x0+offset, y0+offset, x0+offset, y0)) 
        print(self.lines)


    def __init__(self, root, window_height, window_width) -> None:
        self.lines = [] #Stores drawn lines
        #These lists store the start and end points of lines as tuples of two tuples
        self.vert_line_coordinates = []
        self.hori_line_coordinates = []
        #for vali in range(C.cget(height)/10):
        self.size = 20
        self.load_canvas(root, window_height, window_width)

            


    def unload_canvas(self):
        
        self.C.destroy()
    

    
class Saved_project:
    def __init__(self, project:Project) -> None:
        self.drawn_lines = project.lines
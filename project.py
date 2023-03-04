from tkinter import *
from tkinter import ttk, simpledialog
import pickle

class Project:

    def draw_black_line(self, x0, y0, x1, y1):
        return self.C.create_line(x0, y0, x1, y1, fill="black")

    def grid_function(self, size:int, window_width, window_height):
        for i in range(1, 31):
             self.draw_black_line(0, i*size, window_width, i*size)
        for i in range(1, 31):
            self.draw_black_line(i*size, 0, i*size, window_height)
    
    def save_project(self):
        this_project = pickle.dumps(self)
        return this_project

    def load_project(self, root, window_height, window_width):
        self.C = Canvas(root, bg="white",
                height=window_height, width=window_width)
        

        self.grid_function(15, window_width, window_height)
        

        self.C.pack()

    def __init__(self, root, window_height, window_width) -> None:

        self.name = simpledialog.askstring("", "Name the project")
        #for vali in range(C.cget(height)/10):
        self.load_project(root, window_height, window_width)

            


    def unload_canvas(self):
        self.C.destroy()
    

    

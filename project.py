from tkinter import *
from tkinter import ttk, simpledialog

class Project:


    def __init__(self, root, window_height, window_width) -> None:

        self.name = simpledialog.askstring("", "Name the project")
        #for vali in range(C.cget(height)/10):
        def piirra_musta_viiva(x0, y0, x1, y1, self=self):
            return C.create_line(x0, y0, x1, y1, fill="black")

        def grid_function(size:int, window_width, window_height):
            for i in range(1, 31):
                piirra_musta_viiva(0, i*size, window_width, i*size)
            for i in range(1, 31):
                piirra_musta_viiva(i*size, 0, i*size, window_height)
            


        C = Canvas(root, bg="white",
                height=window_height, width=window_width)
        

        grid_function(15, window_width, window_height)
        

        C.pack()

    def unload_canvas():
        C

    

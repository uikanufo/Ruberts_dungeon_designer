from tkinter import *
from tkinter import ttk

def piirra_musta_viiva(x0, y0, x1, y1):
    return C.create_line(x0, y0, x1, y1, fill="black")

def grid_function(size:int, window_width, window_height):
    for i in range(1, 31):
        piirra_musta_viiva(0, i*size, window_width, i*size)
    for i in range(1, 31):
        piirra_musta_viiva(i*size, 0, i*size, window_height)

window_width = 300
window_height = 250

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        fileMenu.add_command(label="New project", )
        fileMenu.add_command(label="Load project", )
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        print(Canvas.configure(self).keys())
        menu.add_cascade(label="Edit", menu=editMenu)
        

    def exitProgram(self):
        exit()
        
root = Tk()
app = Window(root)
C = Canvas(root, bg="white",
           height=window_height, width=window_width)
#for vali in range(C.cget(height)/10):

grid_function(15, window_width, window_height)

C.pack()
root.wm_title("Tkinter window")

root.mainloop()


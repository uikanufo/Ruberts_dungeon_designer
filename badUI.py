from tkinter import *
from tkinter import ttk, simpledialog, filedialog
import pickle
import os
from project import *
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN


window_width = 300
window_height = 300

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        menu = Menu(self.master)
        self.master.config(menu=menu)

        fileMenu = Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        fileMenu.add_command(label="New project", command = self.new_project)
        fileMenu.add_command(label="Save Project", command = self.save_project)
        fileMenu.add_command(label="Load project", command= self.load_project)
        menu.add_cascade(label="File", menu=fileMenu)

        editMenu = Menu(menu)
        editMenu.add_command(label="Undo")
        editMenu.add_command(label="Redo")
        print(Canvas.configure(self).keys())
        menu.add_cascade(label="Edit", menu=editMenu)
        self.current_project = False
    
    def new_project(self):
        if self.current_project.__class__ == Project:
            self.current_project.unload_canvas()
        self.current_project = Project(root, window_height, window_width)
        print("horizontal lines: ", self.current_project.hori_line_coordinates)
        print("vertical lines: ", self.current_project.vert_line_coordinates)

    def exitProgram(self):
        exit()

    
    def save_project(self):
        savable_project = self.current_project.save_project()
        
    def load_project(self):
        project = filedialog.askopenfilename()
        projectbytes = open(project, "rb")
        project = pickle.load(projectbytes)
        project.load_project(root, window_height, window_width)


    



if os.path.isdir("Ruberts_projects") != True:
    os.mkdir("Ruberts_projects")


root = Tk()
app = Window(root)



def draw_rectangle(event):
    x = event.x
    y = event.y
    xstart = x-(x%20)
    ystart = y-(y%20)
    x0 = app.current_project.vert_line_coordinates[int(xstart/20)][0][0]+1
    y0 = app.current_project.hori_line_coordinates[int(ystart/20)][0][1]+1

    x1 = app.current_project.vert_line_coordinates[int((xstart+20)/20)][0][0]+1
    y1 = app.current_project.hori_line_coordinates[int((ystart+20)/20)][0][1]+1
    correct_coords = (x0, y0, x1, y1,)
    print(correct_coords)
    app.current_project.draw_square(correct_coords)





root.bind("<Button>", draw_rectangle)
        

root.wm_title("Tkinter window")

root.mainloop()


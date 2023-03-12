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


def god_help_me(event):
    """I copied this code from Stackoverflow in a desperate attempt to see if it does what I want"""
    canvas = app.current_project.C
    draft = Canvas(app) # if w is deleted, the draft is deleted
    draft.delete(ALL) # if you use the fake canvas for other uses

    concerned = canvas.find_withtag("line") # what you want

    for obj in concerned: # copy on draft

        # first, get the method to use
        if canvas.type(obj) == "line": create = draft.create_line
        # use "elif ..." to copy more types of objects
        else: continue

        # copy the element with its attributes
        config = {opt:canvas.itemcget(obj, opt) for opt in canvas.itemconfig(obj)}
        config["tags"] = str(obj) # I can retrieve the ID in "w" later with this trick
        create(*canvas.coords(obj), **config)

    # use coordinates relative to the canvas
    x = canvas.canvasx(event.x)
    y = canvas.canvasy(event.y)

    item = draft.find_closest(x,y) # ID in draft (as a tuple of len 1)
    if item: item = int( draft.gettags(*item)[0] ) # ID in w
    else: item = None # closest not found

    print(x, y)

def draw_rectangle(event):
    x = event.x
    y = event.y
    xstart = x-(x%20)
    ystart = y-(y%20)
    print(app.current_project.vert_line_coordinates[int(xstart/20)][0][0])
    x0 = app.current_project.vert_line_coordinates[int(xstart/20)][0][0]
    y0 = app.current_project.hori_line_coordinates[int(ystart/20)][0][1]

    x1 = app.current_project.vert_line_coordinates[int((xstart+20)/20)][0][0]
    y1 = app.current_project.hori_line_coordinates[int((ystart+20)/20)][0][1]
    correct_coords = (x0, y0, x1, y1,)
    print(correct_coords)
    app.current_project.draw_square(correct_coords)

   # def mouse_pos(event):
   # x, y = event.x, event.y
   # mouse_place = (x, y)
   # app.current_project.draw_square(mouse_place)  

    """
    Idea:
    Divide x coordinates by grid size
    Round down to nearest (lower) number divisible
    Should give the index in the list
    Repeat for Y
    Same for other corner, but round to higher
    Check where lines intersect
    """ 




root.bind("<Button>", draw_rectangle)
        

root.wm_title("Tkinter window")

root.mainloop()


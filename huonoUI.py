from tkinter import *
from tkinter import ttk, simpledialog, filedialog
import pickle
import os
from project import *


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



        

root.wm_title("Tkinter window")

root.mainloop()


from tkinter import *
from tkinter import ttk, simpledialog, filedialog
import pickle
import os


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
        self.currentProject = False
        

    def exitProgram(self):
        exit()

    def new_project(self):
        self.currentProject = Project()
    
    def save_project(self):
        with open(f"./Ruberts_projects/{self.currentProject.name}.rdproj", "wb") as file:
            saved_project = pickle.dump(self.currentProject, file)
        

    def load_project(self):
        project = filedialog.askopenfilename()
        projectbytes = open(project, "rb")
        return(pickle.load(projectbytes))



if os.path.isdir("Ruberts_projects") != True:
    os.mkdir("Ruberts_projects")


root = Tk()
app = Window(root)


class Project:


    def __init__(self) -> None:

        self.name = simpledialog.askstring("", "Name the project")
        #for vali in range(C.cget(height)/10):
        def piirra_musta_viiva(x0, y0, x1, y1):
            return C.create_line(x0, y0, x1, y1, fill="black")

        def grid_function(size:int, window_width, window_height):
            for i in range(1, 31):
                piirra_musta_viiva(0, i*size, window_width, i*size)
            for i in range(1, 31):
                piirra_musta_viiva(i*size, 0, i*size, window_height)


        C = Canvas(root, bg="white",
                height=window_height, width=window_width)

        grid_function(15, window_width, window_height)

        

root.wm_title("Tkinter window")

root.mainloop()


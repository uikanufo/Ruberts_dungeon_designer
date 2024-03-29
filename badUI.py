from tkinter import *
from tkinter import ttk, simpledialog, filedialog
import pickle
import os
from project import *
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_DOWN
import json


window_width = 300
window_height = 300

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        #These are mainly the buttons for the menu up top. Pretty self-explanatory
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
        save = filedialog.asksaveasfilename()
        with open(save, "w") as saveplace:
            saveplace.write(savable_project)
        
    def load_project(self):
        project = filedialog.askopenfilename()
        self.new_project()
        self.current_project.load_project(project)



root = Tk()
app = Window(root)


def get_square_coordinates(event):

    x = event.x
    y = event.y
    xstart = x-(x%20)
    ystart = y-(y%20)
    x0 = app.current_project.vert_line_coordinates[int(xstart/20)][0][0]+1
    y0 = app.current_project.hori_line_coordinates[int(ystart/20)][0][1]+1

    x1 = app.current_project.vert_line_coordinates[int((xstart+20)/20)][0][0]+1
    y1 = app.current_project.hori_line_coordinates[int((ystart+20)/20)][0][1]+1
    correct_coords = (x0, y0, x1, y1,)
    return correct_coords

def draw_rectangle(event):
    app.current_project.draw_square(get_square_coordinates(event))

def delete_rectangle(event):
    app.current_project.delete_square(get_square_coordinates(event))
    


root.bind("<Button-1 >", draw_rectangle)
root.bind("<Button-3 >", delete_rectangle)
        

root.wm_title("Tkinter window")

root.mainloop()


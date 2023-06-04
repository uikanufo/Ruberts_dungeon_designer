from tkinter import *
from tkinter import ttk, simpledialog
from math import floor 
import json
import pickle

class MemoCanvas(Canvas):
    ''' Canvas subclass that remembers the items drawn on it. '''
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.memo = {}  # Database of Canvas item information.

    # Canvas object constructors.
    def create_line(self, *args, **kwargs):
        id = super().create_line(*args, **kwargs)
        self.memo[id] = dict(type='line', args=args, kwargs=kwargs)
        return id

    def create_rectangle(self, *args, **kwargs):
        id = super().create_rectangle(*args, **kwargs)
        self.memo[id] = dict(type='rectangle', args=args, kwargs=kwargs)
        return id

    def create_image(self, *args, imageinfo=None, **kwargs):
        id = super().create_image(*args, **kwargs)
        if not imageinfo:
            raise RuntimeError('imageinfo dictionary must be supplied')
        del kwargs['image']  # Don't store in memo.
        self.memo[id] = dict(type='image', args=args, imageinfo=imageinfo, kwargs=kwargs)
        return id

    # General methods on Canvas items (not fully implemented - some don't update memo).
    def move(self, *args):
        super().move(*args)

    def itemconfigure(self, *args, **kwargs):
        super().itemconfigure(*args, **kwargs)

    def delete(self, tag_or_id):
        super().delete(tag_or_id)
        if isinstance(tag_or_id, str) and tag_or_id.lower() != 'all':
            if self.memo[tag_or_id]['type'] == 'image':
                del self.imagerefs[tag_or_id]
            del self.memo[tag_or_id]
        else:
            try:
                self.memo.clear()
                del self.imagerefs
            except AttributeError:
                pass


class Project:

    def draw_grey_line(self, x0, y0, x1, y1):
        return self.C.create_line(x0, y0, x1, y1, fill="grey", tags = "bgline") #bgline tag to separate between fore and background

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
        return json.dumps(self.C.memo)

    def load_canvas(self, root, window_height, window_width):
        self.C = MemoCanvas(root, bg="white",
                height=window_height, width=window_width)
        

        self.grid_function(self.size, window_width+1, window_height+1)
        

        self.C.pack()



    def draw_black_line(self, coordinates:tuple):
        self.C.create_line(coordinates[0], coordinates[1], 
                           coordinates[2], coordinates[3], tags = (coordinates, "fgline")) #Meant to correspond to (x0, y0), (x1, y1)
    


    def load_project(self, project):
        # Recreate each saved canvas item.
        with open(project, 'r') as file:
            items = json.load(file)
        for item in items.values():
            if item['type'] == 'line':
                self.C.create_line(*item['args'], **item['kwargs'])


            else:
                raise TypeError(f'Unknown canvas item type: {type!r}')


    def draw_square(self, mouse_coordinates):
        """Draws 4 separate lines that make a square"""
        lining = self.draw_black_line #A shorter way to use the function in question
        x0 = mouse_coordinates[0]
        y0 = mouse_coordinates[1]
        offset = self.size

            
        lining((x0, y0, x0+offset, y0)) 
        lining((x0, y0, x0, y0+offset)) 
        lining((x0+offset, y0+offset, x0, y0+offset)) 
        lining((x0+offset, y0+offset, x0+offset, y0)) 

    def delete_square(self, mouse_coordinates):
        lining = self.C.delete #A shorter way to use the function in question
        x0 = mouse_coordinates[0]
        y0 = mouse_coordinates[1]
        offset = self.size

            
        lining((x0, y0, x0+offset, y0)) 
        lining((x0, y0, x0, y0+offset)) 
        lining((x0+offset, y0+offset, x0, y0+offset)) 
        lining((x0+offset, y0+offset, x0+offset, y0)) 
        
        


    def __init__(self, root, window_height, window_width) -> None:
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
        
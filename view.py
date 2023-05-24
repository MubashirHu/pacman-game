#This file contains the build of the GUI
from tkinter import *
from src.util import *
import time 
class View:

    def __init__(self):
        #GUI window
        self._root = Tk()
        self._canvas = None 
        self._shape_size = 50
        self._wall_color = "blue"
        self._path_color = "black"
        self._pacman_color = "yellow"
        
    def _initialize(self):
        self._root.title('PacMan Game')
        self._root.geometry('800x1000')

        self._canvas = Canvas(self._root, width=800, height=1000, bg='white')
        self._canvas.pack()

    def _draw_shape(self, y_coordinate, x_coordinate, shape):
        if (shape == 1):
            self.add_shape(self, x_coordinate, y_coordinate, self._shape_size, "square", self._wall_color)
            self._root.update()
            return 1
        elif(shape == 0):
            self.add_shape(self, x_coordinate, y_coordinate, self._shape_size, "square", self._path_color)
            self._root.update()
            return 1
        elif(shape == 2):
            self._draw_pacman_in_position(x_coordinate, y_coordinate)
            self._root.update()
            return 1
        else:
            print("ERROR: Unidentified shape")
            self._root.update()
            return 0
        
        

    def _draw_pacman_in_position(self, x_coordinate, y_coordinate):
        self._canvas.delete("pacman")
        self.add_shape(self, x_coordinate, y_coordinate, self._shape_size, "circle", self._pacman_color)

    def add_shape(self, tk_obj, i,j, size, shape, color):
        if shape == "circle":
            #circle
            x0 = i * size
            y0 = j * size
            x1 = x0 + size
            y1 = y0 + size
            self._canvas.create_oval(x0, y0, x1, y1, tags="pacman", fill=color)
        elif shape == "square":
            #rectangle
            x0 = i * size
            y0 = j * size
            x1 = x0 + size
            y1 = y0 + size
            self._canvas.create_rectangle(x0, y0, x1, y1, fill=color)
        else:
            pass
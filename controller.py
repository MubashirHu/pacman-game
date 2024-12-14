#This file is the brain of the file and relays information to and from the model.py and view.py
from model import *
from view import *
from src.util import *
import os
import time
class Controller:
    def __init__(self):
        self.my_model = Model()
        self.my_view = View()

        self.my_view._root.bind("w", lambda event: self._get_user_input("w"))
        self.my_view._root.bind("a", lambda event: self._get_user_input("a"))
        self.my_view._root.bind("s", lambda event: self._get_user_input("s"))
        self.my_view._root.bind("d", lambda event: self._get_user_input("d"))

        self.schedulingSpeed = 400
        self._last_key_pressed = None
        self._last_direction = None
        self._pacman_update_event = 1

        self.direction_map = {
            "w":Direction._up,
            "a":Direction._left,
            "s":Direction._down,
            "d":Direction._right
            }
        
    def _initialize_game(self):
        if self.my_model._initialize():
            if self.my_view._initialize():
                print("Both view and model have been initialized...")

    def _display_initial_positions(self):
        for i in range(self.my_model.Map._rows):
            for j in range(self.my_model.Map._columns):
                location_and_shape = self.my_model._check_for_walls_and_pellet(i, j)       
                self.my_view._draw_shape(location_and_shape[0], location_and_shape[1], location_and_shape[2])     
        
        self.my_view._draw_shape(self.my_model.Pacman._position[0], self.my_model.Pacman._position[1], gamePiece._pacman)

        for i in range (len(self.my_model.Ghosts)):
            self.my_view._draw_ghost(self.my_model.Ghosts[i]._position[0], self.my_model.Ghosts[i]._position[1], self.my_model.Ghosts[i])
       
    def _update_pacman_position(self):
        if self._pacman_update_event is not None:
            self.my_view._root.after_cancel(self._pacman_update_event)

        if self.my_model.Pacman._movement_direction != Direction._idle:
            if self._updated_position_of_pacman_in_model():
                self._updated_position_of_pacman_in_view()
            else:
                self.my_model.Pacman._movement_direction = self._last_direction

        self._pacman_update_event = self.my_view._root.after(self.schedulingSpeed, self._update_pacman_position)  # Schedule

    def _get_user_input(self, direction):

        if direction in self.direction_map:
                if self._last_key_pressed == direction:
                    pass
                else:
                    self.my_model.Pacman._movement_direction = self.direction_map[direction]
                    self._last_key_pressed = direction
                    self._update_pacman_position()
                    
    def _updated_position_of_pacman_in_model(self):

        if self.my_model.Pacman._movement_direction in self.direction_map.values():
                
                next_pacman_direction = self.my_model.Pacman._movement_direction

                _move_valid = self.my_model._is_move_valid(next_pacman_direction)

                if _move_valid:
                        self._last_direction = next_pacman_direction
                        return 1
                else:
                        return 0
        
    def _updated_position_of_pacman_in_view(self):
        self.my_view._draw_shape(self.my_model.Pacman._position[0], self.my_model.Pacman._position[1], gamePiece._pacman) # draw pacman
        return 1
        
    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')
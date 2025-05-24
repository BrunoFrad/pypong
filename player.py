import pygame as pg

from constants import WINDOW_SIZE, PLAYER_SIZE

class Player:
    def __init__(self, width, height, initial_x, initial_y, mode):
        self.width = width
        self.height = height
        self.left = initial_x
        self.top = initial_y
        self.mode = mode

    def handle_keyboard(self):
        keyboard = pg.key.get_pressed()
        if self.mode == 1:
            if keyboard[pg.K_w] and self.top > 20:
                self.top -= 0.1
            elif keyboard[pg.K_s] and self.top < WINDOW_SIZE[1] - PLAYER_SIZE[1] - 20:
                self.top += 0.1
        else:
            if keyboard[pg.K_i] and self.top > 20:
                self.top -= 0.1
            elif keyboard[pg.K_k] and self.top < WINDOW_SIZE[1] - PLAYER_SIZE[1] - 20:
                self.top += 0.1
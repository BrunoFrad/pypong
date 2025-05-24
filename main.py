from constants import PLAYER_SIZE, WINDOW_SIZE, BALL_VELOCITY, BALL_SIZE
from window import Window
from player import Player
from ball import Ball

window = Window()

player_one = Player(PLAYER_SIZE[0], PLAYER_SIZE[1], 80, 300, 1)
player_two = Player(PLAYER_SIZE[0], PLAYER_SIZE[1], 720, 300, 2)
ball = Ball(WINDOW_SIZE[0] / 2, WINDOW_SIZE[1] / 2, BALL_SIZE, BALL_SIZE, BALL_VELOCITY)

window.addObject(player_one)
window.addObject(player_two)
window.addObject(ball)

window.run()
window.destroy()
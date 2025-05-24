from constants import WINDOW_SIZE, PLAYER_SIZE

class Ball:
    def __init__(self, left, top, width, height, velocity):
        self.width = width
        self.height = height
        self.left = left
        self.top = top
        self.velocity = velocity
        self.colliding = False

    def move(self):
        if self.left + self.width >= WINDOW_SIZE[0] - 20 or self.left + self.width < 20:
            self.left = WINDOW_SIZE[0] / 2
            self.top = WINDOW_SIZE[1] / 2

        elif self.top + self.height >= WINDOW_SIZE[1] - 20 or self.top + self.height < 20:
            self.velocity[1] *= -1

        if self.colliding:
            self.velocity[0] *= -1

        self.left += self.velocity[0]
        self.top += self.velocity[1]

    def check_collision(self, player):
        if (self.left < player.left + player.width and
                self.left + self.width > player.left and
                self.top < player.top + player.height and
                self.top + self.height > player.top):
            self.colliding = True
        else:
            self.colliding = False
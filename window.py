import pygame as pg
from constants import WINDOW_SIZE

class Window:

    def __init__(self):
        pg.init()
        self.screen = self.screen = pg.display.set_mode(WINDOW_SIZE)
        pg.display.set_caption('Pong')

        clock = pg.time.Clock()
        clock.tick(60)

        self.objects = []

    def addObject(self, obj):
        self.objects.append(obj)

    def draw(self):
        players = [obj for obj in self.objects if hasattr(obj, 'handle_keyboard')]
        balls = [obj for obj in self.objects if hasattr(obj, 'move')]

        for obj in self.objects:
            if hasattr(obj, 'handle_keyboard'):
                obj.handle_keyboard()
            elif hasattr(obj, 'move'):
                obj.move()

        for ball in balls:
            for player in players:
                    ball.check_collision(player)
                    if ball.colliding:
                        break

        for obj in self.objects:
            pg.draw.rect(self.screen, (255, 255, 255), (obj.left, obj.top, obj.width, obj.height))

    def run(self):
            running = True
            while running:
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        running = False
                self.screen.fill((20, 20, 20))
                self.draw()
                pg.display.flip()

    def destroy(self):
        pg.quit()
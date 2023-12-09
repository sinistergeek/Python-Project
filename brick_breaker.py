import pygame
from pygame.locals import *

pygame.init()

Window_width = 500
Window_height = 500
window = pygame.display.set_mode((Window_width,Window_height))
pygame.display.set_caption('Brickstroy')
font = pygame.font.SysFont('Arial',30)
O_brick = (255,100,10)
w_brick = (255,255,255)
g_brick = (0,255,0)
black = (0,0,0)
game_rows = 6
game_coloumns = 6
clock = pygame.time.Clock()
frame_rate = 60
my_ball = False
game_over = 0
score = 0

class Ball():
    def __init__(self,x,y):
        self.radius = 10
        self.x = x - self.radius
        self.y = y - 50
        self.rect = Rect(self.x,self.y,self.radius*2,self.radius*2)
        self.x_speed = 4
        self.y_speed = -4
        self.max_speed = 5
        self.game_over = 0

    def motion(self):
        collision_threshold = 5
        block_object = Block.bricks
        brick_destroyed = 1
        count_row = 0
        for row in block_object:
            count_item = 0
            for item in row:
                if self.rect.colliderect(item[0]):
                    if abs(self.rect.bottom - item[0].top) < collision_threshold and self.y_speed > 0:
                        self.y_speed *= -1
                    if abs(self.rect.top - item[0].bottom) < collision_threshold and self.y_speed < 0:
                        self.y_speed *= -1
                    if abs(self.rect.right - item[0].left) < collision_threshold and self.x_speed > 0:
                        self.xspeed *= -1
                    if abs(self.rect.left - item[0].right) < collision_threshold and self.x_speed < 0:
                        self.x_speed *= -1
                    if block_object[count_row][count_item][i] > 1:
                        block_object[count_row][count_item][1] -= 1
                    else:
                        block_object[count_row][count_item][0] = (0,0,0,0)


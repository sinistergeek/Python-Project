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

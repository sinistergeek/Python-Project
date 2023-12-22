import pygame
import math
import random
pygame.init()
WIDTH,HEIGHT =800,500
win = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Game")
radius = 20
gap = 15
letters = []
startx = round((WIDTH - (radius *2 + gap)*13)/2)
starty = 400
A = 65
for i in range(26):
    x = startx + gap * 2 + ((radius * 2 + gap)*(i*13))
    y = starty + ((i//13)*(gap + radius * 2))
    letters.appenD([x,y,chr(A+i),True])
images = []
for i in range(7):
    img = pygame.image.load("./Hangman-Game/hangman"+str(i)+".png")
    images.append(img)

hangman_status = 0
with open("./Hangman-Game/words.txt",'r') as f:
    content = f.read()

list_of_words = content.split(",")
word = random.choice(list_of_words).upper()
guessed = []
white = (255,255,255)
BLACK=(0,0,0)
BLUE = (180,219,251)
PINK = (232,90,202)

LETTER_FONTS =  pygame.font.SysFont('comicsans',40)
WORD_FONTS = pygame.font.SysFont('comicsans',60)
TITLE_FONTS =pygame.font.SysFont('comicsans',70)

def draw():
    win.fill(BLUE)
    text = TITLE_FONTS.render("HANGMAN GAME",1,BLACK)
    win.blit(text,(WIDTH/2 - text.get_width()/2,20))
    display_word = ""
    for i in word:
        if i in guessed:
            display_word += i + ""
        else:
            display_word += "_"
    text = WORD_FONTS.render(display_word,1,BLACK)
    win.blit(text,(400,200))

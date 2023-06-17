import pygame
WITDTH, HEIGHT = 800,800
ROWS, COLS = 8,8
SQUARE_SIZE =  WITDTH//COLS

#rgb colors
RED = (171, 56, 48)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
WHITE = (217, 212, 212)
GREY = (128, 128, 128)
BEIGE = (232, 220, 202)

CROWN = pygame.transform.scale(pygame.image.load("crown.png"),(45,25))
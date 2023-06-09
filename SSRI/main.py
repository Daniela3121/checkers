import pygame
from checkers.constants import SQUARE_SIZE, WITDTH,HEIGHT
from checkers.game import Game
#from minimax.algorithm import minimax

FPS = 60
WIN = pygame.display.set_mode((WITDTH, HEIGHT))
pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y// SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row,col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        if game.winner()!= None:
            print(game.winner)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type ==  pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row,col = get_row_col_from_mouse(pos)
                game.select(row,col)

                #piece = board.get_piece(row,col)
                #board.move(piece, 4,3)

        game.update()
    pygame.quit()
main()
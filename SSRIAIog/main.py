import pygame
from checkers.constants import SQUARE_SIZE, WITDTH,HEIGHT,WHITE, RED
from checkers.game import Game
from minimax.algorithm import minimax
from minimax2.algorithm import minimax2
from random_alg.rnd_algorithm import rnd_algorithm

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
        pygame.event.pump()
        clock.tick(FPS)
        
        if game.turn == WHITE:
            '''value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)
            print("Red turn")'''
            
            value, new_board = rnd_algorithm(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)
            print("Red turn")
            
        if game.turn == RED:
            value, new_board = minimax2(game.get_board(), 4, RED, game)
            game.ai_move(new_board)
            print("White turn")

        if game.winner() != None:
            print(game.winner())
            run = False

        '''for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)'''

        game.update()
    
    pygame.quit()

main()

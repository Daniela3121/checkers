import pygame, sys
from button import Button
from checkers.constants import SQUARE_SIZE, WITDTH,HEIGHT,WHITE, RED, BACKGROUND
from checkers.game import Game
from minimax.algorithm import minimax
from minimax2.algorithm import minimax2
from random_alg.rnd_algorithm import rnd_algorithm

pygame.init()

SCREEN = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("Menu")


FPS = 60
WIN = pygame.display.set_mode((WITDTH, HEIGHT))
#pygame.display.set_caption('Checkers')

def get_row_col_from_mouse(pos):
    x,y = pos
    row = y// SQUARE_SIZE
    col = x//SQUARE_SIZE
    return row,col
pygame.init()

#BG = pygame.image.load("assets/Background.png")

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/font.ttf", size)

def main_menu():
    while True:
       #SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("CHECKERS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(410, 100))

        user_no_ai_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(440, 250), 
                            text_input="No AI", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        onlyAI_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(440, 550), 
                            text_input="Only AI", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
                            
        userAI_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(440, 400), 
                            text_input="You & AI", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
                            
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(440, 700), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [user_no_ai_BUTTON, onlyAI_BUTTON, userAI_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if user_no_ai_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_user_no_ai()
                if onlyAI_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_only_ai()
                if userAI_BUTTON.checkForInput(MENU_MOUSE_POS):
                    userAI()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()
        
        
def main_only_ai():
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                print(event)
                if event.key == pygame.K_0:
                    SCREEN.fill("black")
                    main_menu()

        game.update()
    
    pygame.quit()
    
def userAI():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        clock.tick(FPS)
        
        if game.turn == WHITE:
            value, new_board = minimax(game.get_board(), 4, WHITE, game)
            game.ai_move(new_board)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event)
                if event.key == pygame.K_0:
                    SCREEN.fill("black")
                    main_menu()

            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()
def main_user_no_ai():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    while run:
        if game.winner()!= None:
            print(game.winner)

        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print(event)
                if event.key == pygame.K_0:
                    SCREEN.fill("black")
                    main_menu()
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

main_menu()
#main()

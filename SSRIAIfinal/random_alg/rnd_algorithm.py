from copy import deepcopy
import pygame
from random import *
RED = (171, 56, 48)
WHITE = (217, 212, 212)

def rnd_algorithm(position, depth, max_player, game):
    if depth == 0 or position.winner() != None:
        return position.evaluate(), position
    
    if max_player:
        maxEval = float('-inf')
        best_move = None
        print("printing",get_all_moves(position, WHITE,game))
        for move in get_all_moves(position, WHITE, game):
            evaluation = rnd_algorithm(move, depth-1, False, game)[0]
            maxEval = max(maxEval, evaluation)
            if maxEval == evaluation:
                moves = get_all_moves(position, WHITE, game)
                best_move = moves[randint(0, len(moves)-1)]
                #best_move = move
                
        return maxEval, best_move
    else:
        minEval = float('inf')
        best_move = None
        
        for move in get_all_moves(position, RED, game):
            evaluation = rnd_algorithm(move, depth-1, True, game)[0]
            minEval = min(minEval, evaluation)
            if minEval == evaluation:
                moves = get_all_moves(position, RED, game)
                best_move = moves[randint(0, len(moves)-1)]
                best_move = move
        
        #moves = get_all_moves(position, RED, game)
        #best_move = moves[randint(0, len(moves)-1)]
        
        return minEval, best_move


def simulate_move(piece, move, board, game, skip):
    board.move(piece, move[0], move[1])
    if skip:
        board.remove(skip)

    return board


def get_all_moves(board, color, game):
    moves = []
    for piece in board.get_all_pieces(color):
        pygame.event.pump()
        valid_moves = board.get_valid_moves(piece)
        for move, skip in valid_moves.items():
            temp_board = deepcopy(board)
            temp_piece = temp_board.get_piece(piece.row, piece.col)
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board)
    
    return moves

    
    
    
    
    

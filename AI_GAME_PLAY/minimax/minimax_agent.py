import chess

import random

def minimax(board, depth, maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate_board(board), None

    best_moves = []
    if maximizing:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, False)
            board.pop()
            if eval > max_eval:
                max_eval = eval
                best_moves = [move]
            elif eval == max_eval:
                best_moves.append(move)
        return max_eval, random.choice(best_moves)
    else:
        min_eval = float('inf')
        for move in board.legal_moves:
            board.push(move)
            eval, _ = minimax(board, depth - 1, True)
            board.pop()
            if eval < min_eval:
                min_eval = eval
                best_moves = [move]
            elif eval == min_eval:
                best_moves.append(move)
        return min_eval, random.choice(best_moves)

def evaluate_board(board):
    piece_values = {
        chess.PAWN: 1,
        chess.KNIGHT: 3,
        chess.BISHOP: 3,
        chess.ROOK: 5,
        chess.QUEEN: 9,
        chess.KING: 0
    }
    value = 0
    for piece_type in piece_values:
        value += len(board.pieces(piece_type, chess.WHITE)) * piece_values[piece_type]
        value -= len(board.pieces(piece_type, chess.BLACK)) * piece_values[piece_type]

    # Add small noise for variation
    value += random.uniform(-0.1, 0.1)

    if board.is_repetition(3):
        value -= 100 if board.turn == chess.WHITE else -100

    return value


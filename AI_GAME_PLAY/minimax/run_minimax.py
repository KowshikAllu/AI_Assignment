import gym
import gym_chess
import chess
import csv
from minimax_agent import minimax
from utils.recorder import ChessRecorder

# Initialize the chess environment
env = gym.make("Chess-v0")
state = env.reset()
board = chess.Board()  # Local board for minimax and rendering

# Video recorder setup
video = ChessRecorder("gameplay_minimax.mp4")

# Create results CSV file
with open("results_minimax.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Move Number", "Move", "Evaluation"])

    done = False
    move_num = 1

    while not done and not board.is_game_over():
        video.record_frame(board)

        # Run minimax on current board
        eval, move = minimax(board, depth=2, maximizing=board.turn)
        if move is None:
            break  # No legal moves or game over

        print(f"Move {move_num}: {move.uci()} | Eval: {eval}")

        # Play the move in both the environment and local board
        state, reward, done, info = env.step(move)  # gym-chess expects a chess.Move object
        board.push(move)

        writer.writerow([move_num, move.uci(), eval])
        move_num += 1

# Finalize
env.close()
video.release()

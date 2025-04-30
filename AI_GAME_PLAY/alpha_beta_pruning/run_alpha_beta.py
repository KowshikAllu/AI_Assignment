import gym
import gym_chess
import chess
import csv
from alpha_beta_agent import alphabeta
from utils.recorder import ChessRecorder

env = gym.make("Chess-v0")
state = env.reset()
board = chess.Board()  

video = ChessRecorder("gameplay_alpha_beta.mp4")

with open("results_alpha_beta.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Move Number", "Move", "Evaluation"])

    done = False
    move_num = 1
    while not done and not board.is_game_over():
        video.record_frame(board)

        eval, move = alphabeta(board, depth=2, alpha=float('-inf'), beta=float('inf'), maximizing=board.turn)
        if move is None:
            break

        print(f"Move {move_num}: {move.uci()} | Eval: {eval}")

        board.push(move)
        state, reward, done, info = env.step(move)

        writer.writerow([move_num, move.uci(), eval])
        move_num += 1

env.close()
video.release()

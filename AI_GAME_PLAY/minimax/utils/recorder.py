import cv2
import numpy as np
import chess.svg
import cairosvg

class ChessRecorder:
    def __init__(self, output_file):
        self.frames = []
        self.output_file = output_file

    def record_frame(self, board):
        svg = chess.svg.board(board=board).encode("utf-8")
        png = cairosvg.svg2png(bytestring=svg)
        img = cv2.imdecode(np.frombuffer(png, np.uint8), cv2.IMREAD_COLOR)
        img = cv2.resize(img, (512, 512))
        self.frames.append(img)

    def release(self):
        if not self.frames:
            return
        height, width, _ = self.frames[0].shape
        out = cv2.VideoWriter(self.output_file, cv2.VideoWriter_fourcc(*'mp4v'), 1, (width, height))
        for frame in self.frames:
            out.write(frame)
        out.release()

import tkinter as tk
import random
from JigsawBoard import JigsawBoard
from Piece import Piece

class JigsawGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Jigsaw Game")
        self.master.geometry("700x700")

        self.canvas = tk.Canvas(self.master, width=600, height=400, bg="white")
        self.canvas.pack(pady=20)

        self.score_label = tk.Label(self.master, text="Score: 0  Piese schimbate: 0")
        self.score_label.pack()
        self.score = 0

        self.move_counter = 0
        self.max_moves = 25 # Numărul maxim de mutări posibile
        self.pieces_changed = 0

        self.current_piece = None
        self.current_row = 0
        self.current_col = 0

        self.gameHasEnded = False

        self.pieces = [
            Piece("square", 2, 2,"red"),
            Piece("rectangle", 3, 2,"blue"),
            Piece("point", 1, 1,"green"),
            Piece("line", 1, 3,"orange"),
            Piece("backline",3,1,"yellow")
        ]

        self.board = JigsawBoard(8, 12)

        self.draw_board()
        self.place_piece()

    def draw_board(self):
        for i in range(self.board.rows):
            for j in range(self.board.cols):
                x0 = j * 50
                y0 = i * 50
                x1 = x0 + 50
                y1 = y0 + 50
                self.canvas.create_rectangle(x0, y0, x1, y1)

    def place_piece(self):
        if self.gameHasEnded:
            return
        if self.current_piece:
            self.score = self.score + self.current_piece.height * self.current_piece.width
        self.current_piece = random.choice(self.pieces)
        self.redraw_piece()
        self.update_score_label()

    def move_up(self, event=None):
        if self.gameHasEnded:
            return
        if self.current_row > 0:
            self.current_row -= 1
            self.redraw_piece()

    def move_down(self, event=None):
        if self.gameHasEnded:
            return
        if self.current_row + self.current_piece.height < 8:
            self.current_row += 1
            self.redraw_piece()

    def move_left(self, event=None):
        if self.gameHasEnded:
            return
        if self.current_col > 0:
            self.current_col -= 1
            self.redraw_piece()

    def move_right(self, event=None):
        if self.gameHasEnded:
            return
        if self.current_col + self.current_piece.width < 12:
            self.current_col += 1
            self.redraw_piece()

    def change_piece(self, event=None):
        if self.gameHasEnded:
            return
        if self.move_counter == self.max_moves:
            self.lose_game()
            return

        new_piece = self.current_piece
        while new_piece == self.current_piece:
            new_piece = random.choice(self.pieces)
        self.current_piece = new_piece
        self.redraw_piece()

        self.move_counter += 1
        self.update_score_label()

    def redraw_piece(self):
        self.canvas.delete("current_piece")
        x0 = self.current_col * 50
        y0 = self.current_row * 50
        x1 = x0 + self.current_piece.width * 50
        y1 = y0 + self.current_piece.height * 50
        self.canvas.create_rectangle(x0, y0, x1, y1, fill=self.current_piece.color, tags="current_piece")

    def confirm_placement(self, event=None):
        if self.max_moves == self.move_counter:
            self.lose_game()
            return
        if self.gameHasEnded:
            return
        for i in range(self.current_row, self.current_row + self.current_piece.height):
            for j in range(self.current_col, self.current_col + self.current_piece.width):
                if self.board.is_cell_used(i, j):
                    return

        for i in range(self.current_row, self.current_row + self.current_piece.height):
            for j in range(self.current_col, self.current_col + self.current_piece.width):
                self.board.mark_cell_used(i, j)
                self.canvas.create_rectangle(j * 50, i * 50, (j + 1) * 50, (i + 1) * 50, fill=self.current_piece.color)
        self.move_counter += 1

        if self.board.is_full():
            self.win_game()
        else:
            self.place_piece()

    def update_score_label(self):
        self.score_label.config(text="Scor: {} Piese utilizate: {}".format(self.score, self.move_counter))

    def lose_game(self):
        self.gameHasEnded = True
        message = "Ai depășit numărul maxim de piese schimbate. Ai pierdut!\nApasa R pentru a reincepe!"
        self.game_over_label = tk.Label(self.master, text=message)
        self.game_over_label.pack()

    def win_game(self):
        self.gameHasEnded = True
        message = "Felicitări! Ai terminat jocul în {} piese schimbate.\nApasa R pentru a reincepe!".format(self.move_counter)
        self.game_over_label = tk.Label(self.master, text=message)
        self.game_over_label.pack()

    def restart_game(self, event=None):
        self.canvas.delete("current_piece")
        self.canvas.delete("all")  # Clear the canvas
        self.score = 0
        self.move_counter = 0
        self.gameHasEnded = False
        self.board = JigsawBoard(8, 12)
        self.draw_board()  # Redraw the board
        self.place_piece()  # Place a new piece
        if hasattr(self, 'game_over_label'):
            self.game_over_label.pack_forget()

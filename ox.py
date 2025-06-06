import tkinter as tk
from tkinter import messagebox
import copy

class TicTacToeAI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("XO Game with AI")
        self.window.configure(bg="#1e1e1e")
        self.player = "X"
        self.ai = "O"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_buttons()
        self.window.mainloop()

    def create_buttons(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.window, text="", font=('Helvetica', 32), width=5, height=2,
                                command=lambda row=i, col=j: self.player_move(row, col),
                                bg="#292929", fg="white", activebackground="#3c3c3c")
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = btn

    def player_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.player
            self.buttons[row][col]["text"] = self.player
            if self.check_winner(self.board, self.player):
                messagebox.showinfo("Game Over", "You Win!")
                self.reset_board()
                return
            elif self.is_draw(self.board):
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.reset_board()
                return
            self.window.after(300, self.ai_move)  

    def ai_move(self):
        best_score = -float("inf")
        best_move = None
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == "":
                    self.board[i][j] = self.ai
                    score = self.minimax(self.board, 0, False)
                    self.board[i][j] = ""
                    if score > best_score:
                        best_score = score
                        best_move = (i, j)
        if best_move:
            i, j = best_move
            self.board[i][j] = self.ai
            self.buttons[i][j]["text"] = self.ai
            if self.check_winner(self.board, self.ai):
                messagebox.showinfo("Game Over", "AI Wins!")
                self.reset_board()
            elif self.is_draw(self.board):
                messagebox.showinfo("Game Over", "It's a Draw!")
                self.reset_board()

    def minimax(self, board, depth, is_max):
        if self.check_winner(board, self.ai):
            return 1
        if self.check_winner(board, self.player):
            return -1
        if self.is_draw(board):
            return 0

        if is_max:
            best = -float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = self.ai
                        best = max(best, self.minimax(board, depth + 1, False))
                        board[i][j] = ""
            return best
        else:
            best = float("inf")
            for i in range(3):
                for j in range(3):
                    if board[i][j] == "":
                        board[i][j] = self.player
                        best = min(best, self.minimax(board, depth + 1, True))
                        board[i][j] = ""
            return best

    def check_winner(self, b, mark):
        # Check rows, columns, diagonals
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] == mark: return True
            if b[0][i] == b[1][i] == b[2][i] == mark: return True
        if b[0][0] == b[1][1] == b[2][2] == mark: return True
        if b[0][2] == b[1][1] == b[2][0] == mark: return True
        return False

    def is_draw(self, b):
        for row in b:
            for cell in row:
                if cell == "":
                    return False
        return True

    def reset_board(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""

# Run game
if __name__ == "__main__":
    TicTacToeAI()

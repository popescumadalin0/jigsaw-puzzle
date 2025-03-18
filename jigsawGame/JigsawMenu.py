import tkinter as tk
from functools import partial

class JigsawMenu:
    def __init__(self, master, start_callback):
        self.master = master
        self.master.title("Meniu Joc")
        self.master.geometry("400x300")

        self.start_callback = start_callback

        tk.Label(master, text="Selectează dificultatea:", font=("Arial", 14)).pack(pady=10)

        self.difficulty_var = tk.StringVar(value="mediu")

        difficulties = {
            "Ușor": 40,
            "Mediu": 30,
            "Greu": 25,
            "Imposibil": 20
        }

        for difficulty, attempts in difficulties.items():
            tk.Radiobutton(master, text=difficulty, variable=self.difficulty_var, value=attempts).pack(anchor="w")

        tk.Button(master, text="Start Joc", command=self.start_game).pack(pady=20)

    def start_game(self):
        attempts = int(self.difficulty_var.get())
        self.master.destroy()  # Închide fereastra meniului
        self.start_callback(attempts)
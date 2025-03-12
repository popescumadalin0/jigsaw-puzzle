

import tkinter as tk
from JigsawGame import JigsawGame
from ControllerInput import ControllerInput

if __name__ == "__main__":
    root = tk.Tk()
    app = JigsawGame(root)
    controller = ControllerInput(app)
    root.mainloop()

import tkinter as tk
from JigsawGame import JigsawGame
from ControllerInput import ControllerInput
import pygame

from JigsawMenu import JigsawMenu


def start_game(attempts):
    root = tk.Tk()
    app = JigsawGame(root, attempts)

    pygame.init()
    controller_connected = pygame.joystick.get_count() > 0
    if not controller_connected:
        print("PS5 controller not detected. Using keyboard controls.")
    else:
        pygame.joystick.init()
        joystick = pygame.joystick.Joystick(0)
        joystick.init()

    controller = ControllerInput(app) if controller_connected else None

    while True:
        if controller_connected:
            controller.handle_input()
        else:
            root.bind("<Up>", lambda event: app.move_up())
            root.bind("<Down>", lambda event: app.move_down())
            root.bind("<Left>", lambda event: app.move_left())
            root.bind("<Right>", lambda event: app.move_right())
            root.bind("<space>", lambda event: app.change_piece())
            root.bind("<Return>", lambda event: app.confirm_placement())
            root.bind("r", lambda event: app.restart_game())

        root.update_idletasks()
        root.update()


if __name__ == "__main__":
    menu_root = tk.Tk()
    JigsawMenu(menu_root, start_game)
    menu_root.mainloop()  # Pornește meniul
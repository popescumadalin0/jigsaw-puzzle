class ControllerInput:
    def __init__(self, game):
        self.game = game
        self.game.master.bind("<Up>", self.game.move_up)
        self.game.master.bind("<Down>", self.game.move_down)
        self.game.master.bind("<Left>", self.game.move_left)
        self.game.master.bind("<Right>", self.game.move_right)
        self.game.master.bind("<space>", self.game.change_piece)
        self.game.master.bind("<Return>", self.game.confirm_placement)
        self.game.master.bind("r", self.game.restart_game)

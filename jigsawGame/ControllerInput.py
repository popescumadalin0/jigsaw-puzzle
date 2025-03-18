import pygame
class ControllerInput:
    def __init__(self, game):
        self.game = game
        self.last_move_time = pygame.time.get_ticks()  # Timpul ultimei mișcări
        self.move_delay = 250  # Delay-ul în milisecunde între mișcări
        self.last_direction = None  # Ultima direcție de mișcare
        self.last_move_direction = None  # Ultima direcție de mișcare efectuată

    def handle_input(self):
        current_time = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.JOYBUTTONDOWN:
                if event.button == 0:  # X button on PS5 controller
                    self.game.change_piece()
                elif event.button == 3:  # Square button on PS5 controller
                    self.game.confirm_placement()
                elif event.button == 1:  # R2 button on PS5 controller
                    self.game.restart_game()
            elif event.type == pygame.JOYAXISMOTION:
                if current_time - self.last_move_time > self.move_delay:
                    if event.axis == 1:  # Vertical axis
                        if event.value < -0.5:
                            self.game.move_up()
                            self.last_move_time = current_time
                        elif event.value > 0.5:
                            self.game.move_down()
                            self.last_move_time = current_time
                    elif event.axis == 0:  # Horizontal axis
                        if event.value < -0.5:
                            self.game.move_left()
                            self.last_move_time = current_time
                        elif event.value > 0.5:
                            self.game.move_right()
                            self.last_move_time = current_time

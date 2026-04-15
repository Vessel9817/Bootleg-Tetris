#!/usr/bin/python3

# import necessary modules
import pygame

from .block import Block
from .grid import Grid


def start_game(display: pygame.surface.Surface) -> None:
    '''Is responsible for: parsing key inputs and redirecting them to controls within the game; for drawing and refreshing the display and grid; for checking whether a player has lost or not and prompting the respective message for such an event and; for the countdown timers of auto dropping and automatically locking the blocks to their respective grids'''
    grid_1 = Grid(100, 100, 400, display)
    grid_2 = Grid(500, 100, 400, display)
    key_pressed_actions = {
        # Player 1 controls
        pygame.K_w     : grid_1.block.rotate_cw,
        pygame.K_a     : grid_1.block.move_left,
        pygame.K_s     : grid_1.block.move_down,
        pygame.K_d     : grid_1.block.move_right,
        pygame.K_t     : grid_1.block.rotate_180,
        pygame.K_f     : grid_1.block.rotate_ccw,
        pygame.K_g     : grid_1.block.hard_drop,
        pygame.K_h     : grid_1.swap_hold,

        # Player 2 controls
        pygame.K_KP8   : grid_2.block.rotate_cw,
        pygame.K_KP5   : grid_2.block.move_down,
        pygame.K_KP4   : grid_2.block.move_left,
        pygame.K_KP6   : grid_2.block.move_right,
        pygame.K_i     : grid_2.block.rotate_180,
        pygame.K_j     : grid_2.block.rotate_ccw,
        pygame.K_k     : grid_2.block.hard_drop,
        pygame.K_l     : grid_2.swap_hold
    }
    clock = pygame.time.Clock()

    # Event loop
    while True:
        # Displaying game over
        if grid_1.lose:
            grid_2.win = True
            font = pygame.font.SysFont(None, 30)
            new_game_text = font.render("Press Space To Restart", False, Block.WHITE)
            display.blit(new_game_text, (display.get_width() / 2.75, 50))
        elif grid_2.lose:
            grid_1.win = True
            font = pygame.font.SysFont(None, 30)
            new_game_text = font.render("Press Space To Restart", False, Block.WHITE)
            display.blit(new_game_text, (display.get_width() / 2.75, 50))

        # Handling game events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif not (grid_1.win or grid_2.win):
                # Performing key press incurred operations
                if event.type == pygame.KEYDOWN:
                    if event.key in key_pressed_actions:
                        key_pressed_actions[event.key]()
                    else:
                        # Unknown key pressed
                        pass
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                pygame.draw.rect(display, Block.BLACK, pygame.Rect(display.get_width()/2.75, 50, 600, 50))
                grid_1.reset_grid()
                grid_2.reset_grid()

        # Dropping blocks
        if not (grid_1.win or grid_2.win):
            for g in Grid.GRIDS:
                g.drop_counter += 1

                # Delaying block movements
                if g.drop_counter >= Grid.SPEED:
                    g.drop_counter = 0

                    g.block.auto_move_down()
                    g.draw_level()

                # Continuing block auto-lock timer
                if g.timer_running:
                    g.timer += 1

                # Checking if block can move down
                elif g.block.detect_collision(r_off=-1):
                    g.timer_running = True

        # Repainting grids
        for g in Grid.GRIDS:
            g.draw_block()
            g.draw_grid()

        # Refreshing display at 60fps
        pygame.display.update()
        clock.tick(60)

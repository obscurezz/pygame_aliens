import sys

import pygame

from settings import Settings
from ship import Ship, Ufo


class AlienInvasion:
    """Class for resource manipulation and behavior of the game"""

    def __init__(self):
        """Game initialization and crating game resources"""
        pygame.init()
        self.settings = Settings()
        # Set game display mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption('Alien Invasion')
        # Set the ship on the screen
        self.ship = Ship(self)
        self.ufo = Ufo(self)

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _update_screen(self):
        # Every loop is coloring the screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.ufo.blitme()
        # Outputs the last drawn screen
        pygame.display.flip()

    def run_game(self):
        """Starting main loop of the game"""
        while True:
            # Checking for user keyboard-input events
            self._check_events()
            self.ship.update()
            self._update_screen()


if __name__ == '__main__':
    # Creating the object and starting the game
    ai = AlienInvasion()
    ai.run_game()

import pygame


class Ship():
    def __init__(self, ai_game):
        """Initializing the ship and sets its start position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Loads the ship's image and gets the rectangle
        self.image = pygame.image.load('images/ship1.png')
        self.rect = self.image.get_rect()
        # Each new ship start at the middle bottom position of screen
        self.rect.midbottom = self.screen_rect.midbottom
        # Counted position of the ship
        self.x = float(self.rect.x)
        # Moving flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.rect.x -= self.settings.ship_speed

        # Updating rect based on self.x
        # self.rect.x = self.x

    def blitme(self):
        """Drawing the ship to the current position"""
        self.screen.blit(self.image, self.rect)


class Ufo():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Loads the ship's image and gets the rectangle
        self.image = pygame.image.load('images/ufo1.png')
        self.rect = self.image.get_rect()
        # Each new ship start at the middle bottom position of screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Drawing the ship to the current position"""
        self.screen.blit(self.image, self.rect)

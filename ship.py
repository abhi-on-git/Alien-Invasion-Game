import pygame


class Ship():

    def __init__(self, screen, ai_settings):
        """Initialising ship and its starting position"""
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading ship image and its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Starting each ship at the bottom of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Storing a decimal value for ships center (because centerx cannot store a float value)
        self.center = float(self.rect.centerx)

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Updates the ship position based on position flag"""
        # Updates Center var not the actual centerx variable
        # This and operator limits the ships range to be in the visible 'screen'
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor

        # Updating rect object from self.center

        self.rect.centerx = self.center

    def blitme(self):
        """Draw the current position of the ship"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Centers the spaceship on the screen"""
        self.center = self.screen_rect.centerx

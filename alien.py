import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to just represent a single alien in the fleet"""

    def __init__(self, ai_settings, screen):
        """Setting alien up and its strating position"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Loading the alien image and its attributes
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start the aliens at the top left of the scrren

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

    def blitme(self):
        """This draws the alien onto the screen"""
        self.screen.blit(self.image, self.rect)
        self.rect.x = self.x

    def check_edges(self):
        """Checks if alien has hit edge of screen and returns true if yes"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Moves the alien right"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x





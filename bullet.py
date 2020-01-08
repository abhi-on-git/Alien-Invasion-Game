import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """A class to manage the bullets fired from the ship"""

    def __init__(self, ai_settings, screen, ship):
        """Creates a bullet object at the ships initial position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # First we are going to create a bullet rect at (0,0) then set the correct position

        # This statement below is incorporating the original position and also the bullets
        # height and width
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        # Now placing the bullets at the right place
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        self.colour = ai_settings.bullet_colour
        self.speed_factor = ai_settings.bullet_speed_factor

        # Storing the y co-ordinate as a float so we can make minute changes

        self.y = float(self.rect.y)

    def update(self):
        """Moving the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y -= self.speed_factor
        # Now updating the actual rect position of the bullet
        self.rect.y = self.y

    def draw_bullet(self):
        """This will draw the bullet onto the screen"""
        pygame.draw.rect(self.screen, self.colour, self.rect)

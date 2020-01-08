from settings import Settings
from pygame.sprite import Group
import pygame
from game_stats import GameStats
from ship import Ship
import game_functions as gf


def run_game():
    # Initialising game and creating screen object and settings
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    stats = GameStats(ai_settings)
    # Make a Ship
    ship = Ship(screen, ai_settings)
    # Making a group to store bullets and a group to store aliens
    bullets = Group()
    aliens = Group()

    # Creating fleet of alien
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # starting the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
        gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


run_game()


import sys
from bullet import Bullet
from alien import Alien
import pygame
from time import sleep


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Responds to keypress"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)


def check_keyup_events(event, ship):
    """Responds to keypress"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Responds to keyboard entries and mouse clicks"""
    # Watching for keyboard and mouse events (inputs).
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, aliens, bullets):
    """Updates the images o the screen and flips to a new screen"""
    screen.fill(ai_settings.bg_colour)
    # Redrawing all bullets behind ship and alien
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    # Draw function draws every element in the group on to the 'screen' on the specified
    # rect spot
    aliens.draw(screen)
    # Make the most recent screen drawn visible (refreshing...)
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    bullets.update()

    # Now deleting the bullets otherwise they will take up unnecessary space
    # We shouldn't remove items from a list in a for loop, so we copy it here
    # using the copy() method - from game_function : update_scree()

    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    """Checks and responds to bullet and alien collisions"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """Fire a bullet if bullet limit has not reached"""
    # Creating a new bullet and adding it to the screen
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """Determines the number of aliens that fit in a row"""
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determining the number of rows of aliens that fit on the screen"""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Creates an alien and then places it in a row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    alien.rect.x = alien.x
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship,  aliens):
    """Creates full fleet of aliens"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Creating the fleet of aliens

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def check_fleet_edges(ai_settings, aliens):
    """Checks if aliens have hit the edge of screen"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """Drops the entire fleet and changes alien direction"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Responds approprately to alien hitting a ship"""
    # Decrement ships left
    stats.ships_left -= 1

    # Empty list of aliens and bullets
    aliens.empty()
    bullets.empty()

    # Create a new fleet and then center ship
    create_fleet(ai_settings, screen, ship, aliens)
    ship.center_ship()

    # Pause
    sleep(0.5)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Updates the entire position of the alien fleet"""
    check_fleet_edges(ai_settings, aliens)
    # Alien-ship collisions
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    aliens.update()



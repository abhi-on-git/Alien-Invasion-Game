class Settings():
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Initialising Game Settings"""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_colour = (230, 230, 230)

        # Ship Settings
        self.ship_speed_factor = 0.5
        self.ship_limit = 3

        # Bullet settings

        self.bullet_speed_factor = 1
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullet_colour = (60, 60, 60)
        self.bullets_allowed = 7

        # Alien settings

        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 10
        # Value of 1 means right and -1 means left direction
        self.fleet_direction = 1
